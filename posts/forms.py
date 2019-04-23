from django import forms
from .models import Opro

class OproForm(forms.ModelForm):
    class Meta:
        model = Opro
        fields = '__all__'