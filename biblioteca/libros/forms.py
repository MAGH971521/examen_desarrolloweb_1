from django import forms
from .models import Libros


class LibrosModelForms(forms.ModelForm):
    Nombre = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Nombre del Libro',
            'class': 'form-control'}))
    Autor = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Autor',
            'class': 'form-control'}))
    Editorial = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'Editorial: ',
            'class': 'form-control'}))
    ISBN = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder': 'ISBN del Libro',
            'class': 'form-control'}))
    Precio = forms.FloatField(label='', widget=forms.NumberInput(
        attrs={
            'placeholder': 'Precio',
            'class': 'form-control'}))

    class Meta:
        model = Libros
        fields = [
            "Nombre",
            "Autor",
            "Editorial",
            "ISBN",
            "Precio",
        ]
