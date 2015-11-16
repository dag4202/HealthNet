from django.contrib import admin

from main_patient.models import Patient, Doctor, Nurse, procedure, prescription, SystemAdmin

# class AdminPatient(admin.ModelAdmin):
# 	list_display = ('sex','dob')
admin.site.register(SystemAdmin)
admin.site.register(Patient)
admin.site.register(Nurse)
admin.site.register(Doctor)
admin.site.register(procedure)
admin.site.register(prescription)
