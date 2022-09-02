#from http.client import HTTP5Response
from django.http import HttpResponse 
from django.shortcuts import render

# Create your views here.

def home(request):
    print("i am view")
    return HttpResponse("This is Home page") 