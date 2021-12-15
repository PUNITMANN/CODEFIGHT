from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,"index.html")


def python(request):
    return render(request,"blog/python.html/")

def html(request):
    return render(request,"blog/html.html/")

def css(request):
    return render(request,"blog/css.html/")

def javascript(request):
    return render(request,"blog/javascript.html/")