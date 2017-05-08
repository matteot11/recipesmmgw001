from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import Nationalities, Profile
from django.contrib.auth.models import User

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    #return HttpResponse('Hello World!')
    return render(request, 'index.html')

@csrf_exempt
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
        return render(request, 'registration/loggedin.html', {'username': request.user.username})
    else:
        #messages.error(request, 'Invalid login credentials')
        return render(request, 'index.html', {'error': True})

'''
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        print "merda"
        login(request, user)
        # Redirect to a success page.
        return render(request, 'registration/loggedin.html')
    else:
        # Return an 'invalid login' error message.
        return render(request, 'index.html')
'''
#def index(request):
#    r = requests.get('http://httpbin.org/status/418')
#    print(r.text)
#    return HttpResponse('<pre>' + r.text + '</pre>')

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
            #user = User.objects.create_user(username=username, password=confirm_password, email=email)
            user = User(username=username, password=confirm_password, email=email)
            user.save()
            profile = Profile(user=user, nationality=kind_of_cousine)
            profile.save()
            return render(request, 'register.html', {'error': error, 'registration_completed': True})

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')


'''
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

'''