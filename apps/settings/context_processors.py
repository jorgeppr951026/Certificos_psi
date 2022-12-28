from operator import imod
from django.shortcuts import render
from apps.settings.models import Settings
# Create your views here.

def extras(request):
    company_settings = Settings.objects.first()
    if  company_settings == None:
        company_settings = Settings()
        company_settings.company_name = 'Empresa'
        company_settings.miniature = 'general/logo.png'
        company_settings.logo = 'general/mini.png'
        company_settings.save()
    return {'company_settings':company_settings}
    
