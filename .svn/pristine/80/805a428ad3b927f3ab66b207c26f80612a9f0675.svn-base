from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import Group,User
from main.models import LogEntry
from main.forms import ViewPatientsForm
from calender.views import reminders
from main_patient.models import Patient, procedure, prescription
from django.forms.models import inlineformset_factory
from hospital.forms import HospitalForm, DepartmentForm

@login_required
def main(request):
        is_Doctor = request.user.groups.filter(name = 'Doctor').exists()
        is_Patient = request.user.groups.filter(name ='Patient').exists()
        is_Nurse = request.user.groups.filter(name = 'Nurse').exists()
        is_Admin = request.user.groups.filter(name = 'Sys Admin').exists()
        is_Super = request.user.is_superuser
        reminder=reminders(request)
        if is_Doctor:
                doctor = request.user.doctor
                view_patients_form = ViewPatientsForm(doctor = doctor)
                return render(request, 'main.html', {'is_Admin' : is_Admin, 
                'is_Doctor' : is_Doctor, 'is_Nurse' : is_Nurse, 'is_Patient' : is_Patient, 'is_Super': is_Super,'reminders' : reminder, 'view_patients_form': view_patients_form})
        return render(request, 'main.html', {'is_Admin' : is_Admin, 
                'is_Doctor' : is_Doctor, 'is_Nurse' : is_Nurse, 'is_Patient' : is_Patient, 'is_Super' : is_Super, 'reminders' : reminder})


@login_required
def logView(request):
	log = LogEntry.objects.all().order_by('datetime')
	#output = '\n '.join([p.description for p in log])
	return render(request, 'log.html', {'log': log})

@login_required
def SelectPatient(request):
        doctor = request.user.doctor
        view_patients_form = ViewPatientsForm(request.POST, doctor = doctor)
        if view_patients_form.is_valid():
                patient = view_patients_form.cleaned_data['patients']
                return HttpResponseRedirect('/select/patient/' + str(patient.id) + '/')
        else:
                return HttpResponseRedirect('/')
                
@login_required        
def UpdateMI(request, patient_id):
        patient = Patient.objects.get(pk = patient_id)
        doctor = request.user.doctor
        PrescriptionFormSet = inlineformset_factory(Patient, prescription)
        ProcedureFormSet = inlineformset_factory(Patient, procedure)
        if request.method == "POST":
                prescription_form = PrescriptionFormSet(request.POST, request.FILES, instance=patient)
                procedure_form = ProcedureFormSet(request.POST, request.FILES, instance = patient)
                if prescription_form.is_valid() and procedure_form.is_valid():
                        prescription_form.save()
                        procedure_form.save()
                        prescription_form = PrescriptionFormSet(instance = patient)
                        procedure_form = ProcedureFormSet(instance = patient)
                else:
                        print(prescription_form.errors, procedure_form.errors)
        else:
                prescription_form = PrescriptionFormSet(instance = patient)
                procedure_form = ProcedureFormSet(instance = patient)
        return render(request, 'myPatients.html', {'patient':patient, 'prescription_form': prescription_form, 'procedure_form': procedure_form})

@login_required
def switchAccept(request):
	user = request.user
	if user.doctor.accepting == True:
		user.doctor.accepting = False
	else:
		user.doctor.accepting = True
	user.doctor.save()

	return HttpResponseRedirect('/')
