from django.db import models
from django.core import validators

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=20, validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(20)
    ])
    apellido = models.CharField(max_length=20, validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(20)
    ])
    correo = models.CharField(max_length=50, validators=[
        validators.EmailValidator("El correo debe llevar @")
    ])