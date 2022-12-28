from django.db import models
from django.urls import reverse
# Create your models here.


cargo = (
    ("Especialista","Especialista"),
    ("Director(a)" , "Director(a)"),
)

class Asesorador(models.Model):

    name = models.CharField("Nombre", max_length=250)
    cargo = models.CharField("Cargo", max_length=250,   default="Especialista")

    class Meta:
        verbose_name = "Asesorador"
        verbose_name_plural = "Asesoradores"

    def __str__(self): 
        return self.name

    


class Dictaminador(models.Model):

    name = models.CharField("Nombre", max_length=250)
    cargo = models.CharField("Cargo", max_length=250,  default="Especialista")
    correo = models.CharField("Correo", max_length=250,  default=" ")

    class Meta:
        verbose_name = "Dictaminador"
        verbose_name_plural = "Dictaminadores"

    def __str__(self): 
        return self.name

    

class Certificador(models.Model):

    name = models.CharField("Nombre", max_length=250)
    cargo = models.CharField("Cargo", max_length=250 ,  default="Especialista")
    tomo = models.CharField("Tomo", max_length=250)
    folio = models.CharField("Folio", max_length=250)
    numero = models.CharField("Numero", max_length=250, default=" ")

    class Meta:
        verbose_name = "Certificador"
        verbose_name_plural = "Certificadors"

    def __str__(self):
        return self.name

    

class Cliente(models.Model):

    codigo = models.CharField("Codigo", max_length=250, primary_key=True)
    name = models.CharField("Nombre", max_length=250)
    organismo = models.CharField("Organismo", max_length=250, default=" ")


    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f'{self.codigo} - {self.name}'

   

class PSI(models.Model):

    fecha = models.DateField("Fecha", auto_now=False, auto_now_add=False)
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)     
    asesorador = models.ForeignKey(Asesorador, verbose_name="Asesorador", on_delete=models.CASCADE)     
    dictaminador = models.ForeignKey(Dictaminador, verbose_name="Dictaminador", on_delete=models.CASCADE)
    certificador = models.ForeignKey(Certificador, verbose_name="Certifcador", on_delete=models.CASCADE)
    estado = models.BooleanField(default=False, choices=((False,"Pendiente"),(True,"Certificado")))

    class Meta:
        verbose_name = "PSI"
        verbose_name_plural = "PSIs"

    def __str__(self):
        return f'{self.fecha} - {self.cliente.name}'

    def get_absolute_url(self):
        return reverse("PSI_detail", kwargs={"pk": self.pk})


class Certifico(models.Model):
    code = models.CharField("Codigo", max_length=250, unique=True)
    fecha = models.DateField("Fecha", auto_now=False, auto_now_add=False)
    psi = models.ForeignKey(PSI, verbose_name="Plan de Seguridad", on_delete=models.CASCADE) 
    estado = models.BooleanField(default=False, choices=((False,"Pendiente"),(True,"Certificado")))

    class Meta:
        verbose_name = "Certifico"
        verbose_name_plural = "Certificos"

    def __str__(self):
        return f'{self.fecha} - {self.psi.cliente.name}'

   