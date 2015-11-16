from django.conf.urls import patterns, url
from main_patient import views

urlpatterns = patterns('',
	url(r'^load', views.upload, name='upload'),
	url(r'^doctor', views.RegisterDoctor, name='regDoctor'),
	url(r'^nurse', views.RegisterNurse, name='regNurse'),
	url(r'^admin', views.RegisterAdmin, name='regAdmin'),
    url(r'^medicalInfo', views.export, name = 'export'),
	url(r'^$', views.Register, name='register'),
)
