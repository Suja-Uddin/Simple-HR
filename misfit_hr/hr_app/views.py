from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import connection
from collections import namedtuple
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.urls import reverse
from django.db.models import Q

import re
from .models import User, Request, UserForm


def login(request):
    if 'user' in request.session:
        return HttpResponseRedirect('/requests')
    data = {}
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            if "signupButton" in request.POST:
                users = User.objects.get(Q(name=request.POST['name'])|Q(email=request.POST['email']))
                if users:
                    data['sign_up_failure'] = True
                else:
                    imageFile = request.FILES['myImage'].file.read()
                    user = User(name=request.POST['name'], email=request.POST['email'], image=imageFile)
                    user.save()
                    data['sign_up_success'] = True
            else:
                try:
                    user = User.objects.get(name = request.POST['name'], email = request.POST['email'])
                except User.DoesNotExist:
                    user = None
                if user:
                    user.is_logged_in = True
                    user.save()
                    request.session['user'] = user.id
                    return HttpResponseRedirect('/requests')
                data['user_not_found'] = True
    else:
        userForm = UserForm()
    data['loginForm'] = userForm
    data['signupForm'] = UserForm()
    return render(request, 'login.html', data)


def request(request):
    if 'user' in request.session:
        print("session user: ", request.session['user'])
        data = {}
        user = User.objects.get(id=request.session['user'])
        if request.method == 'POST':
            print("Creating request")
            req = Request(details = request.POST['request_details'], requester_id=user.id, status = '1')
            req.save()
            return JsonResponse({'request_saved': True})

        data['user'] = user
        if user.type == '1':
            requests = Request.objects.filter(requester_id=user.id)
        elif user.type == '2':
            requests = Request.objects.all()
        else:
            requests = Request.objects.filter(status='2')
        for idx, req in enumerate(requests):
            print(idx, req)
            requested_user = User.objects.get(id=req.requester_id)
            if req.processor_id:
                processor_user = User.objects.get(id=req.processor_id)
                requests[idx].processor_user = processor_user
            requests[idx].requested_user = requested_user
            # requestList.append({})
        print(requests)
        data['requests'] = requests
        return render(request, 'request.html', data)
    else:
        return HttpResponseRedirect('/')


def logout(request):
    user = User.objects.get(id=request.session['user'])
    user.is_logged_in = False
    user.save()
    del request.session['user']
    return HttpResponseRedirect('/')

def updateRequest(request, request_id):
    if 'user' in request.session:
        req = Request.objects.get(id=request_id)
        if request.method == 'POST':
            if 'requestDetails' in request.POST:
                req.details = request.POST['requestDetails']
            if 'requestStatus' in request.POST:
                req.status = request.POST['requestStatus']
            req.save()
            return HttpResponseRedirect('/requests')
        data = {}
        user = User.objects.get(id = request.session['user'])
        data['user'] = user
        data['req'] = req
        return render(request, 'request-update.html', data)
    return  HttpResponseRedirect('/')
