import pymssql

from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin  

from apps.certificacion.models import Cliente


def parser(str):
    str = str.replace('µ','Á')
    str = str.replace('\x90','É')
    str = str.replace('Ö','Í')
    str = str.replace('à','Ó')
    str = str.replace('é','Ú')
    str = str.replace('\xa0','á')
    str = str.replace('\x82','é')
    str = str.replace('¡','í')
    str = str.replace('¢','ó')
    str = str.replace('£','ú')
    
    return str
   

class ConSQL(LoginRequiredMixin,View):
    DB_HOST = '192.168.1.246' 
    DB_USER = 'sa' 
    #port=1433,
    DB_PASS = 'VERSAT123*' 
    DB_NAME = 'Prueba' 

    def get(self, reques, *args, **kwargs):
        try:
            conn = pymssql.connect(server=self.DB_HOST , user=self.DB_USER, password=self.DB_PASS , database=self.DB_NAME, charset='UTF-8' )  
            
            cursor = conn.cursor() 
            query = 'SELECT code, name, organ  FROM Prueba.dbo.usuario' 
            cursor.execute(query)  
            
            
            if query.upper().startswith('SELECT'): 
                data = cursor.fetchall()   # Traer los resultados de un select 
            else: 
                conn.commit()              # Hacer efectiva la escritura de datos 
                data = None 
            
            cursor.close()                 # Cerrar el cursor 
            conn.close()                   # Cerrar la conexión 

            cleintes = Cliente.objects.all().values('codigo')
            client_list = []

            for cl in cleintes:
                client_list.append(cl['codigo']) 


            for val in data:
                if not val[0] in client_list:
                    client = Cliente.objects.create(codigo = parser(val[0]), name = parser(val[1]), organismo = parser(val[2]))
                    client.save()
                   
            return redirect('/cliente/list/')
           
        except Exception as e:
            print('%s' % type(e))
            return redirect('/cliente/list/')

      
