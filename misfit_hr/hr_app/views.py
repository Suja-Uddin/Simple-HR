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
from .models import User, Request, UserForm

def login(request):
    data = {}
    if request.method == 'POST':
        print("post method")
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            print(request.POST['name'])
            user = User.objects.filter(name=request.POST['name']).first()
            print(user)
            if user:
                return HttpResponseRedirect('/requests')
            data['user_not_found'] = True
    else:
        userForm = UserForm()
    data['loginForm'] = userForm
    print(data)
    return render(request, 'login.html', {'loginForm': userForm})

def request(request):
    return render(request, 'index.html', {})