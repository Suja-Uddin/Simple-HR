from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q

from .models import User, Request, UserForm


def login(request):                     # Login and Signup handler view.
    if 'user' in request.session:       # Authenticated user -> requests page
        return HttpResponseRedirect('/requests')
    data = {}
    if request.method == 'POST':        # performs a login or signup
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            if "signupButton" in request.POST:  # signup request
                user_form = UserForm()
                if User.objects.filter(Q(name=request.POST['name']) | Q(email=request.POST['email'])).count():
                    data['sign_up_failure'] = True  # Duplicate name / email
                else:
                    image_file = request.FILES['myImage'].file.read()
                    user = User(name=request.POST['name'], email=request.POST['email'], image=image_file)
                    user.save()
                    data['sign_up_success'] = True
            else:       # login request
                try:
                    user = User.objects.get(name=request.POST['name'], email=request.POST['email'])
                except User.DoesNotExist:       # invalid credential
                    user = None
                if user:
                    user.is_logged_in = True
                    user.save()
                    request.session['user'] = user.id
                    return HttpResponseRedirect('/requests')
                data['user_not_found'] = True
    else:
        user_form = UserForm()
    data['loginForm'] = user_form
    data['signupForm'] = UserForm()
    return render(request, 'login.html', data)


def handle_request(request):        # Request index page and request create
    if 'user' in request.session:
        data = {}
        user = User.objects.get(id=request.session['user'])
        if request.method == 'POST':    # Create request
            req = Request(details=request.POST['request_details'], requester_id=user.id, status='1')
            req.save()
            return JsonResponse({'request_saved': True})

        data['user'] = user
        if user.type == '1':    # Employee: Show user specific requests
            requests = Request.objects.filter(requester=user)
        elif user.type == '2':  # HR: Show all requests
            requests = Request.objects.all()
        else:                   # Manager: Show HR reviewed requests
            requests = Request.objects.filter(status='2')

        for idx, req in enumerate(requests):    # Add requester and processor info
            requests[idx].requested_user = User.objects.get(id=req.requester.id)
            if req.processor:       # Request processor exists
                requests[idx].processor_user = User.objects.get(id=req.processor.id)
        data['requests'] = requests
        return render(request, 'request.html', data)

    return HttpResponseRedirect('/')        # Not authorized


def logout(request):    # log out view
    user = User.objects.get(id=request.session['user'])
    user.is_logged_in = False
    user.save()
    del request.session['user']     # removing from session
    return HttpResponseRedirect('/')


def update_request(request, request_id):        # Update request details / status
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        req = Request.objects.get(id=request_id)
        if request.method == 'POST':
            if 'requestDetails' in request.POST:    # Change details from Employee
                req.details = request.POST['requestDetails']
            if 'requestStatus' in request.POST:     # Change status from HR/Manager
                req.status = request.POST['requestStatus']
                if request.POST['requestStatus'] == '3':    # Save processor info
                    req.processor = user
            req.save()
            return HttpResponseRedirect('/requests')
        data = {'user': user, 'req': req}
        return render(request, 'request-update.html', data)
    return HttpResponseRedirect('/')        # Not authorized
