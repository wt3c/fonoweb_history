from django import forms
from .models import Holder


class HolderForm(forms.ModelForm):
    class Meta:
        model = Holder
        fields = "__all__"
        exclude = ('owner', )
