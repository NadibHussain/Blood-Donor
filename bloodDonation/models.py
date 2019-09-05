from django.db import models
from django import forms
# Create your models here.



class Donator(models.Model):

    Sex_choice = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30,choices=Sex_choice)
    contact_number = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    blood_type= models.CharField(max_length=10)
    location= models.CharField(max_length=255,null=True)
    joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class AddDoner(forms.ModelForm):
    class Meta:
        model=Donator
        fields=['name','sex','contact_number']
