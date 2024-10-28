from django.contrib import admin
from appAutores.models import Autor

# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display=['nombre', 'apellido', 'correo']
    
admin.site.register(Autor)