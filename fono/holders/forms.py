from django import forms

class HoldersForm(forms.Form):
    nome = forms.CharField()
