from django import forms
from .models import Holder, Pseudonym
from .models import Society


class HolderForm(forms.ModelForm):
    # society_combom = forms.ModelChoiceField(queryset=Society.objects.all())
    class Meta:
        model = Holder
        fields = "__all__"
        exclude = ('owner',)


class PseudonymForm(forms.ModelForm):
    class Meta:
        model = Pseudonym
        fields = "__all__"
