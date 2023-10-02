from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def helloworld(request):
    return HttpResponse('Hello World')

def homePage(request):
    return render(request, 'healthy/home.html')

def yourName(request, name):
    return render(request, 'healthy/yourname.html', {'name': name})