
from io import BytesIO
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from core.settings import TEMPLATE_DIR, BASE_DIR
import webbrowser

import os
from apps.certificacion.models import *
from pyreportjasper import PyReportJasper




def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse("Error Rendering PDF", status=400)


class PDF(View):

    def get(self, request, *args, **kwargs):
     

        certifico =  Certifico.objects.get(id = kwargs['pk'])
        certifico.estado = True
        certifico.save()
        psi = PSI.objects.get(id = certifico.psi.id)
        psi.estado = True
        psi.save()
        
        
        #REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
        #input_file = os.path.join(REPORTS_DIR, 'Certifico.jrxml')
        output_file = os.path.dirname(BASE_DIR) + f'/Dictamenes/{certifico.code} ({certifico.psi.cliente})'
        input_file = TEMPLATE_DIR + "/certificacion/pdf/Certifico.jrxml"
        image_url = TEMPLATE_DIR + "/certificacion/pdf/desoft.png"
        
        pyreportjasper = PyReportJasper()
        pyreportjasper.config(
        input_file,
        output_file,
        output_formats=["pdf", "docx"],
        parameters={
            'code': certifico.code,
            'cliente': certifico.psi.cliente.name,
            'organismo': certifico.psi.cliente.organismo,
            'fecha': str(certifico.fecha.strftime("%d.%m.%Y")),
            'certificador': certifico.psi.certificador.name ,
            'tomo': certifico.psi.certificador.tomo,
            'folio': certifico.psi.certificador.folio,
            'numero': certifico.psi.certificador.numero,
            'cargo': certifico.psi.certificador.cargo,
            'dictaminador': certifico.psi.dictaminador.name,
            'dict_cargo': certifico.psi.dictaminador.cargo,
            'correo': certifico.psi.dictaminador.correo,
            'implementador': certifico.psi.asesorador.name,
            'url': image_url,
            
        
        },
        locale='en_US'
        )
      
        pyreportjasper.process_report()
        
        
        #webbrowser.open_new(f'{output_file}.pdf')
        url = self.request.META.get('HTTP_REFERER')

        with open(f'{output_file}.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline;filename={certifico.code} ({certifico.psi.cliente}).pdf'
            

        if 'pendiente' in str(url):
            return redirect('/certifico/pendiente/list/')
        
        #return redirect('/certifico/list/')
        return response


data = {
    "company": "Dennnis Ivanov Company",
    "address": "123 Street name",
    "city": "Vancouver",
    "state": "WA",
    "zipcode": "98663",


    "phone": "555-555-2345",
    "email": "youremail@dennisivy.com",
    "website": "dennisivy.com",
}

# Opens up page as PDF


class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        object = Certifico.objects.get(id=kwargs['pk'])
        data['object'] = object
       
        pdf = render_to_pdf('certificacion/pdf/pdf_template.html', data)

        return HttpResponse(pdf, content_type='application/pdf')


# Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        object = Certifico.objects.get(id=kwargs['pk'])
        data['object'] = object
        if 'm/s' in object.indicador_viento_Iw:
            data['viento_km'] = round((float(object.var_ff) * 3.6), 2)
            data['viento_m'] = round((float(object.var_ff)), 2)
            data['viento_kn'] = round((float(object.var_ff) * 1.943), 2)
            data['precip_in'] = round((float(object.var_RRR) * 0.039), 2)
        else:
            data['viento_km'] = round((float(object.var_ff) * 1.85), 2)
            data['viento_m'] = round((float(object.var_ff) * 0.514), 2)
            data['viento_kn'] = round((float(object.var_ff)), 2)
            data['precip_in'] = round((float(object.var_RRR) * 0.039), 2)
        pdf = render_to_pdf('tiempo/pdf/pdf_template.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f'{object.var_IIiii}-{object.fecha}-{object.hora}.pdf'
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
