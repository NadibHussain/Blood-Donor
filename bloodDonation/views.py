from django.shortcuts import render
from django.http import HttpResponse
from .models import Donator
from django.db.models import Q
from . import forms
# Create your views here.
def doner_list(request):
    donors =Donator.objects.all()
    # print(donors)
    if(request.method == "POST"):
        search=request.POST["search"]
        category=request.POST["category"]
        if(category=="all"):
            donors = Donator.objects.filter(Q(name__icontains=search)|
            Q(contact_number__icontains=search)|
            Q(age__icontains=search)|
            Q(sex__icontains=search)|
            Q(blood_type__icontains=search))
        elif(category=="name"):
            donors = Donator.objects.filter(Q(name__icontains=search))
        elif(category=="bloodType"):
            donors = Donator.objects.filter(Q(blood_type__icontains=search))
        elif(category=="age"):
            donors = Donator.objects.filter(age__icontains=search)
        elif(category=="number"):
            donors = Donator.objects.filter(contact_number__icontains=search)
        elif(category=="location"):
            donors = Donator.objects.filter(location__icontains=search.capitalize())
        return render(request,'bloodDonation/list.html',{'doners':donors})
    return render(request,'bloodDonation/list.html',{'doners':donors})


def new_doner(request):
    form=forms.AddDoner()
    return render(request,'bloodDonation/newDoner.html',{'form':form})