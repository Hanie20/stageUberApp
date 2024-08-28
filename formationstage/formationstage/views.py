from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def mapresentation(request):
    return render(request, "informations.html")

def apropos(request):
    return render(request,"about.html")

def services(request):
    return render(request, "nos-services.html")