from django import forms
from . import models
class AddDoner(forms.ModelForm):

    class Meta:
        model=models.Donator
        fields=['name','location','contact_number','age']
