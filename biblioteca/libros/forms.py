from django import forms
from .models import Libros


class LibrosModelForms(forms.ModelForm):
    class Meta:
        model = Libros
        fields = [
            "Nombre",
            "Autor",
            "Editorial",
            "ISBN",
            "Precio",
        ]
