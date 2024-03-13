from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
ppl=[]

class Person:
    def __init__(self,Uname,password):
        self.Uname=Uname
        self.password=password

def add(request):
    if request.method=='POST':
        Uname=request.POST.get('Uname')
        password=request.POST.get('password')
        person=Person(Uname=Uname,password=password)
        people.append(person)
    return render(request,"APP1/add.html")

def list(request):
    return render(request,"APP1/list.html",{'people':people})
