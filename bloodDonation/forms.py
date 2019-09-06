from django import forms
from . import models
class AddDoner(forms.ModelForm):

    class Meta():
        model=models.Donator
        fields=['name','location','contact_number','age']
    
    
    def clean_contact_number(self):
        num=self.cleaned_data['contact_number']
        if (num[:3]!='+88'):
            num='+88'+num
            return num
        return self.cleaned_data['contact_number']
        