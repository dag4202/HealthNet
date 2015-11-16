from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from main_patient.models import Patient 
from main_patient.models import Doctor
from hospital.models import Hospital 

class Entry(models.Model):
	
	#These are from the appointment class
	"""
    notes = models.CharField(max_length=300) #converted to snippet
    description = models.CharField(max_length=300) #converted to body
    patient = models.ForeignKey('main_patient.Patient')
    doctor = models.ForeignKey('main_doctor.Doctor')
    hospital = models.ForeignKey('hospital.Hospital')
    procedure = models.OneToOneField('procedure.Procedure')
	"""

	#ToDo
	"""
	#make these work
	patient = models.ForeignKey('main_patient.Patient') 
	doctor = models.ForeignKey('main_doctor.Doctor')
    hospital = models.ForeignKey('hospital.Hospital')
    procedure = models.OneToOneField('procedure.Procedure')

	"""
	# patient = models.ForeignKey('main_patient.Patient')

	#These are from calendar
	title = models.CharField(max_length = 40)
	snippet = models.CharField(max_length=150,blank = True)
	creator = models.ForeignKey(User,blank=True, null = True)
	body = models.TextField(max_length=10000,blank=True)
	date = models.DateField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	remind = models.BooleanField(default = False)
	location = models.CharField(max_length=50,blank = True)
	patient = models.ForeignKey('main_patient.Patient')
	doctor = models.ForeignKey('main_patient.Doctor',limit_choices_to = {'accepting' : True})
	#hospital = models.ForeignKey('hospital.Hospital')
	#procedure = models.OneToOneField('procedure.Procedure')
	def __str__(self):
		if (self.title):
			return str(self.creator) + " - " + self.title
		else:
			return str(self.creator) + " - " + self.snippet[:40]
	def short(self):
		if self.snippet:
			return "<i>%s</i> - %s" %(self.title,self.snippet)
		else:
			return self.title
	short.allow_tags = True
	class Meta:
		verbose_name_plural = "entries"

class EntryAdmin(admin.ModelAdmin):
	list_display = ["creator", "date", "title", "snippet","location"]
	search_fields = ["title", "snippet", "date"]
	list_filter = ["creator"]

