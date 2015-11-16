from django.conf.urls import patterns, url
from hospital import views


urlpatterns = patterns('',
	url(r'^hospital', views.CreateHospital, name = 'hospitals'),
	url(r'^department', views.CreateDepartment, name = 'department'),
	url(r'^$', views.CreateHospital, name='hospital'),
)