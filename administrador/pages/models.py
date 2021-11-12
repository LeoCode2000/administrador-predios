from django.db import models

# Create your models here.
class Predio(models.Model):
    tipo_choice = [('urbano', 'Urbano'),
                ('rural', 'Rural')
    ]

    cedula_catastral = models.CharField(null=True, unique=True, max_length=50, verbose_name="cedula catastral") 
    direccion = models.CharField( max_length=200, unique=True, verbose_name = "direccion")
    tipo = models.CharField(max_length=40, choices=tipo_choice)

    def __str__(self):
        return self.direccion

class Propietario(models.Model):
    nombre = models.CharField(null=True, max_length=100, verbose_name="nombre")
    identificacion = models.CharField(unique=True, max_length=50, verbose_name="identificacion")
    
    def __str__(self):
        return self.identificacion

class Matricula(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)

