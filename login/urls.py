from django.conf.urls import patterns, url
from login import views

urlpatterns = patterns('',
	url(r'^$', views.user_login, name = "views.user_login"),
)