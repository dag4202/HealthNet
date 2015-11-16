from django.contrib.auth.models import User
from hospital.models import Hospital, Departments
from django import forms

class HospitalForm(forms.ModelForm):
	class Meta:
		model = Hospital
		fields = ('name', 'address_line1', 'address_line2', 'city', 'state', 'zip_code', 'department')

class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Departments
		fields = ('deps',)