from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.utils import timezone
from main.models import LogEntry



def user_login(request):
  context = RequestContext(request)
  if request.method == 'POST':
    if 'login' in request.POST:
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user:
        login(request, user)
        entry = LogEntry(username=username, datetime=timezone.now(), description='user login')
        entry.save()
        return HttpResponseRedirect(request.GET.get('next', '/'))
      else:
        return render_to_response('login.html', {'username': username, 'error': "Invalid email or password."}, context)
    elif 'register' in request.POST:
      return render_to_response('register.html', {'username': username}, context)
  else:
    if request.user.is_authenticated():
      if request.GET.get('logout', '') == 'true':
        logout(request)
        entry = LogEntry(username='none', datetime=timezone.now(), description='user logout')
        entry.save()
      return HttpResponseRedirect(request.GET.get('next', '/'))
    return render_to_response('login.html', {}, context)