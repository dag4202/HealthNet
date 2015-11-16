from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
#from calender import views
from login import views
from main_patient.views import Modify_Profile, export
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'healthNet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', include('main.urls', namespace="main")),
    url(r'^select/', include('main.urls', namespace="select")),
    url(r'^create', include('hospital.urls', namespace="hospitals")),
    url(r'^export/', include('main_patient.urls', namespace = 'export')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls', namespace="login")),
    url(r'^reg', include('main_patient.urls', namespace="admin register")),
    url(r'^up', include('main_patient.urls', namespace="upload")),
    url(r'^profile/', include('main_patient.urls', namespace="profile")),
    url(r'^update/', Modify_Profile),
    url(r'^register/', include('main_patient.urls', namespace="register")),
    url(r'^calendar/', include('calender.urls', namespace="calender")),
    url(r'^system', include('main.urls', namespace="log")),
    url(r'^up', include('main_patient.urls', namespace="upload")),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
