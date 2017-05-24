from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import Nationalities, Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

ingredient_list = []

def index(request):
    #return HttpResponse('Hello World!')
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user.username)
        profile = Profile.objects.get(user_id=user.id)
        nationality = profile.nationality
        nationalities = Nationalities.objects.all().order_by("nationality")

        return render(request, 'mainPage.html', {'username': request.user.username, 'nationality': nationality, 'nationalities': nationalities, 'ingredient_list': ingredient_list})
    else:
        return render(request, 'index.html')


def login(request):

    # here you get the post request username and password
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    # authentication of the user, to check if it's active or None
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        # this is where the user login actually happens, before this the user
        # is not logged in.
        auth.login(request, user)

        #return render(request, 'registration/loggedin.html')
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user_id=user.id)
        nationality = profile.nationality
        nationalities = Nationalities.objects.all().order_by("nationality")

        return render(request, 'mainPage.html', {'username': username, 'nationality': nationality, 'profile': profile, 'nationalities': nationalities, 'ingredient_list': ingredient_list})

    else:
        #messages.error(request, 'Invalid login credentials')
        #return render(request, 'index.html', {'error': True})
        messages.error(request, 'Invalid login credentials')
        return redirect('index')


def logout(request):
    # message user or whatever
    return auth.logout(request)


def loggedin (request):
    return render_to_response('registration/loggedin.html',
                              {'username': request.user.username})  #use render instead


def registration_page(request):
    nationalities = Nationalities.objects.all().order_by("nationality")
    return render(request, 'register.html', {"nationalities": nationalities, 'registration_completed':False})


def registration_request(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        kind_of_cousine = request.POST.get('kind_of_cousine', '')
        confirm_password = request.POST.get('confirm_password', '')

        nationalities = Nationalities.objects.all().order_by("nationality")

        error = False
        message = ''

        user_exist = User.objects.filter(username=username)

        if(username == ""):
            message='Invalid username'
        elif user_exist.exists():
            message = 'Username already exists'
        elif (email == ""):
            message = 'Invalid e-mail'
        elif(password == ""):
            message = 'Invalid password'
        elif(password != confirm_password):
            message = 'Password and confirm password are different'
        elif(kind_of_cousine == "null"):
            message = 'Insert the nationality'

        if message != '':
            error = True
            return render(request, 'register.html',{'error': error, 'message': message, "nationalities": nationalities, 'registration_completed':False})
        else:
            user = User.objects.create_user(username=username, password=confirm_password, email=email)
            profile = Profile(user=user, nationality=kind_of_cousine)
            profile.save()
            return render(request, 'register.html', {'error': error, 'registration_completed': True})


def registration_complete(request):
    return render_to_response('registration/registration_complete.html')


def update_list(request):
    if 'Insert' in request.POST:
        new_ingredient = request.POST.get('new_ingredient')
        ingredient_list.append(new_ingredient)
        return render(request, 'mainPage.html', {'username': request.user.username, 'ingredient_list': ingredient_list})
    if 'Delete' in request.POST:
        ingredient_list[:] = []
        #return render(request, 'mainPage.html', {'username': request.user.username, 'ingredient_list': ingredient_list})
        return index(request)

def info(request):
    return render(request, 'info.html', {'user': request.user})

