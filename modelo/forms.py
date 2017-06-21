from django import forms

class UploadImageForm(forms.Form):
    arquivo = forms.ImageField()
