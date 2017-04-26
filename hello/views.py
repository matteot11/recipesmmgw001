from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Nationalities

# Create your views here.
def index(request):
    #return HttpResponse('Hello World!')
    #return render(request, 'index.html')

    nationalities = Nationalities.objects.all()
    return render(request, 'index.html', {'nationalities': nationalities})

#def index(request):
#    r = requests.get('http://httpbin.org/status/418')
#    print(r.text)
#    return HttpResponse('<pre>' + r.text + '</pre>')


'''
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

'''