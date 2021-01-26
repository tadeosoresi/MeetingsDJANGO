#API FORMS
from django import forms

class FormularioRegistro(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField() 
    usuario = forms.CharField()
    email = forms.EmailField()
    tel = forms.IntegerField()
    sex = forms.CharField()
    provincia = forms.CharField()
    codigo_postal = forms.IntegerField()