from django.db import models
#from localflavor.us.models import USStateField
# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=250)
    address_line1 = models.CharField(max_length = 128)
    address_line2 = models.CharField(max_length = 128, blank = True)
    city = models.CharField(max_length = 64)
    state = models.CharField(max_length = 2)
    zip_code = models.CharField(max_length = 5)
    department = models.ManyToManyField('Departments')
    
    def __str__(self):
    	return self.name
class Departments(models.Model):
    DEPT_CHOICES = (('AD', 'Admitting'), ('A', 'Autism Center'), ('B', 'Billing'),
     ('CBDC', 'Cancer and Blood Disorders Center'), ('CCU', 'Cancer Care Unit'), ('DS', 'Dentistry'),
     ('D', 'Diabetes'), ('P', 'Pharmacy'), ('PS', 'Plastic Surgery'))
    deps = models.CharField(max_length = 5,choices = DEPT_CHOICES)
    def __str__(self):
    	return self.deps