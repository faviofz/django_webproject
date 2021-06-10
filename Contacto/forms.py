from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=20, required=True)
    email = forms.CharField(label="Email", max_length=30, required=True)
    contenido = forms.CharField(label="Mensaje", widget=forms.Textarea)