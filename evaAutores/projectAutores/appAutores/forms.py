from django import forms
from appAutores.models import Autor
class FormAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        
        def clean(self):
            user_clean_data = super().clean()

            inputNombre = user_clean_data['nombre']
            if len(inputNombre) > 20:
                raise forms.ValidationError("El largo máximo del nombre son 20 caracteres..")
            elif len(inputNombre) < 3:
                raise forms.ValidationError("El mínimo de este campo son 3 caracteres..")
            
            inputApellido = user_clean_data['apellido']
            if len(inputApellido) > 20:
                raise forms.ValidationError("El largo máximo del apellido son 20 caracteres..")
            elif len(inputApellido) < 3:
                raise forms.ValidationError("El mínimo de este campo son 3 caracteres..")
            
            inputCorreo = user_clean_data['correo']
            if len(inputCorreo) > 50:
                raise forms.ValidationError("El largo máximo del correo son 50 caracteres..")
            elif len(inputCorreo) < 3:
                raise forms.ValidationError("El mínimo de este campo son 3 caracteres..")
            
            return inputNombre, inputApellido, inputCorreo