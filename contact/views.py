from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contactFrom(request):
    return render(request, 'contact.html')