from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em>My Second Project</em>")


def example(request):
    exampledict = {'example_insert':'EXAMPLE PAGE'}
    return render(request,'appTwo/example.html',context=exampledict)

def help(request):
    helpdict = {'help_insert':'HELP *_* PAGE'}
    return render(request,'appTwo/help.html',context=helpdict)
