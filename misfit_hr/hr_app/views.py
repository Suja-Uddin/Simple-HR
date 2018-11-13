from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
import urllib.request
import re
from . import models

def login(request):
    if request.method == 'POST':
        userForm = models.UserForm(request.POST)
        if userForm.is_valid():
            return HttpResponseRedirect('/requests')
    else:
        userForm = models.UserForm()
    return render(request, 'login.html', {'loginForm': userForm})

def request(request):
    return render(request, 'index.html', {})