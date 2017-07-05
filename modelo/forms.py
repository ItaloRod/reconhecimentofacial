from django import forms

class UploadImageForm(forms.Form):
    arquivo = forms.ImageField(label="insira aqui", widget = forms.FileInput(attrs={'color':'yellow'}))
