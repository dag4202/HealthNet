from django.conf.urls import patterns, url
from calender import views

urlpatterns = patterns('calender.views',
	#url(r"^settings/$", "settings", name='settings'),
	url(r"^month/(\d+)/(\d+)/(prev|next)/$", "month", name='month'),
    url(r"^month/(\d+)/(\d+)/$", "month", name='month'),
    url(r"^month$", "month", name='month'),
    url(r"^day/(\d+)/(\d+)/(\d+)/$", "day", name='day'),
	url(r'^$', "main", name='main'),
)