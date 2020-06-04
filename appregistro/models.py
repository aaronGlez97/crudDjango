from django.db import models
#aqui definire los modelos de mi app para diseñar el CRUD
# Create your models here.


#definiendo el modelo registro 
class Registro(models.Model):
    nombre=models.CharField(max_length=30)
    correo=models.CharField(max_length=30)
    telefono=models.IntegerField()
    domicilio=models.CharField(max_length=100)

