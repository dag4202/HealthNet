from django import forms
from main_patient.models import Patient, Doctor



class ViewPatientsForm(forms.Form):
    patients = forms.ModelChoiceField(Patient.objects.none(), widget= forms.Select())
    def __init__(self, *args, **kwargs):
        doctor = kwargs.pop('doctor')
        super(ViewPatientsForm, self).__init__(*args, **kwargs)
        self.fields['patients'].queryset = doctor.patientlist.all()
