from django import forms
from .models import Holder, Pseudonym


class HolderForm(forms.ModelForm):
    class Meta:
        model = Holder
        fields = "__all__"
        exclude = ('owner',)


class PseudonymForm(forms.ModelForm):
    class Meta:
        model = Pseudonym
        fields = "__all__"
