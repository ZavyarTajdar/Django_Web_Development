from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World, From Zavyar At Home Page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello World, From Zavyar At About Page")

def contact(request):
    return HttpResponse("Hello World, From Zavyar At Contact Page")

