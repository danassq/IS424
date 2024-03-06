from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("THIS IS A SITE TO CALCULATE TAX")

tax=0.15
def calc(request,num):
    taxed=(num*tax)+num
    return HttpResponse(f"price after tax {taxed}")

def taxrate(request):
    return HttpResponse(f"<h1 style=\"color:blue\">tax rate is {tax*100}%</h1>")
