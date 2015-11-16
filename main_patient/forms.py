from django.contrib.auth.models import User
from main_patient.models import Patient, Nurse, Doctor, SystemAdmin
from django import forms
from django.forms import extras
from django.forms.models import inlineformset_factory

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')

class AdminForm(forms.ModelForm):
    class  Meta:
        model = SystemAdmin
        fields = ('hospital',)


class PatientProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=extras.SelectDateWidget(years=range(2015,1900,-1)), label = "DOB:", required = True);
    insurance = forms.CharField(label = "Insurance Provider:")
    insuranceNum = forms.IntegerField(label = "Insurance Number:")

    class Meta:
        model = Patient
        fields = ('sex', 'dob', 'insurance', 'insuranceNum')
"""
class PatientMedicalForm(forms.ModelForm):
    prescriptions = forms.CharField(widget = forms.Textarea,label = "Current prescriptions and doses")
    medicalinfo = forms.CharField(widget = forms.Textarea,label = "Patient's medical information")
    pastmedicalinfo = forms.CharField(widget = forms.Textarea,label = "Patient's past medical history")

    class Meta:
        model = PatientMedical
        fields = ('prescriptions', 'medicalinfo', 'pastmedicalinfo')
"""            

class DoctorProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=extras.SelectDateWidget(years=range(2015,1900,-1)), label = "DOB:", required = True);
    joined = forms.DateField(widget=extras.SelectDateWidget(years=range(2015,1900,-1)), label = "Joined:", required = True);
    class Meta:
        model = Doctor
        fields = ('sex', 'department', 'location', 'phone', 'joined', 'certification',
            'schooling', 'specialty', 'residency', 'fellowship', 'dob', 'hospital','patientlist')

class NurseProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=extras.SelectDateWidget(years=range(2015,1900,-1)), label = "DOB:", required = True);
    joined = forms.DateField(widget=extras.SelectDateWidget(years=range(2015,1900,-1)), label = "Joined:", required = True);
    class Meta:
        model = Nurse
        fields = ('sex', 'department', 'location', 'phone', 'joined', 'certification',
            'schooling', 'residency', 'dob', 'hospital')


# class Patient_Profile_Form(forms.Form):
#     fname = forms.CharField(label = "First Name:")
#     lname = forms.CharField(label = "Last Name:")
#     username = forms.CharField(label = "username",required = False)
#     password = forms.CharField(widget = forms.PasswordInput, required = True)
#     password2 = forms.CharField(widget = forms.PasswordInput, required = True)
#     dob = forms.DateField(label = "DOB:", required = True);
#     email = forms.EmailField(label = "Email:")
#     insurance = forms.CharField(label = "Insurance Provider:")
#     insuranceNum = forms.IntegerField(label = "Insurance Number:")
#     # widgets= {
#     #     'password'  : forms.PasswordInput(),
#     #     'password2'  : forms.PasswordInput(),
#     # }
#     def cleanPassword2(self):
#         password1 = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
 
#         if not password2:
#             raise forms.ValidationError("You must confirm your password")
#         if password1 != password2:
#             raise forms.ValidationError("Your passwords do not match")
#         return password2
