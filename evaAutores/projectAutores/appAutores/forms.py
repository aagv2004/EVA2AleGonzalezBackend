from django import forms
from appAutores.models import Autor
class FormAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'