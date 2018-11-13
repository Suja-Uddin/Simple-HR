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

def index(request):
    print("here")
    if request.method == 'POST':
        userForm = models.UserForm(request.POST)
        # if form.is_valid():
        #     return
    else:
        userForm = models.UserForm()

    return render(request, 'index.html', {'loginForm': userForm})