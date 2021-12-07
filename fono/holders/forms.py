from django import forms
from .models import Holder


class HoldersForm(forms.ModelForm):
    class Meta:
        model = Holder
        fields = "__all__"
