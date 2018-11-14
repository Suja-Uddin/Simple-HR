from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.urls import reverse

import re
from .models import User, Request, UserForm

def login(request):
    data = {}
    if request.method == 'POST':
        print("post method")
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            print(request.POST['name'])
            # user = User.objects.filter(name=request.POST['name']).first()
            try:
                user = User.objects.get(name = request.POST['name'], email = request.POST['email'])
            except User.DoesNotExist:
                user = None
            print(user)
            if user:
                user.is_logged_in = True
                user.save()
                request.session['user'] = user.id
                return HttpResponseRedirect('/requests')
            data['user_not_found'] = True
    else:
        userForm = UserForm()
    data['loginForm'] = userForm
    print(data)
    return render(request, 'login.html', data)

def request(request):
    if 'user' in request.session:
        print("session user: ", request.session['user'])
        data = {}
        user = User.objects.get(id = request.session['user'])
        data['user'] = user
        print(data['user'])
        return render(request, 'request.html', data)
    else:
        return HttpResponseRedirect('/')
def logout(request):
    user = User.objects.get(id = request.session['user'])
    user.is_logged_in = False;
    user.save()
    del request.session['user']
    return HttpResponseRedirect('/')
