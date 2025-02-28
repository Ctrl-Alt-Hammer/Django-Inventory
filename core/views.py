#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, Django!")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("My About Page!")
    return render(request, 'about.html')