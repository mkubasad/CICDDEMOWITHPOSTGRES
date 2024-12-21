from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from . import models
from . import forms

# Create your views here.

def home(request): 
    context = {}
    return render(request, template_name="demo/home.html", context=context)

def createDoctor(request):
    print("***createDoctor: ", request.method)
    if request.method == 'GET':
        form = forms.DoctorForm()
        context = {"form":form}
        return render(request, template_name="demo/createDoctor.html", context=context)
    if request.method == 'POST':
        print("*********POST:", request.POST)
        print("*********FILES:", request.FILES)
        form = forms.DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            doctor = models.Doctor()
            doctor.first_name = form.cleaned_data['first_name']
            doctor.last_name = form.cleaned_data['last_name']
            doctor.gender = form.cleaned_data['gender']
            doctor.speciality = form.cleaned_data['speciality']
            doctor.contact_number = form.cleaned_data['contact_no']
            doctor.board_reg_no = form.cleaned_data['board_reg_no']
            doctor.average_time_per_patient = form.cleaned_data['average_time_per_patient']
            doctor.active = form.cleaned_data['active']
            systemSeq = models.Sequence.objects.get(pk="DR")
            last_number = systemSeq.last_number+1
            
            
            doctor.system_reg_no = systemSeq.prefix+f'{last_number:>010}'
            if request.FILES.get('board_reg_cert'):
                doctor.board_reg_cert = request.FILES['board_reg_cert']
            doctor.save()
            systemSeq.last_number = last_number
            systemSeq.save()
            messages.add_message(request, messages.INFO, 'Information saved for doctor: '+str(doctor))
            return redirect(reverse('demo:home', kwargs={}))