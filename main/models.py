from django.db import models
from hospital.models import Hospital
#from django.contrib.auth.models import User


class LogEntry(models.Model):
	#user = models.OneToOneField(User, related_name='user_actor_name')
	username = models.CharField(max_length=50)
	datetime = models.DateTimeField()
	description = models.CharField(max_length=50)
	#hospital = models.ForeignKey('hospital.Hospital')

	def __str__(self):
		return self.username + " " + self.datetime + " " + self.description
# Create your models here.
