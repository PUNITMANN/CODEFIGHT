from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

def index(request):
    return render(request,"blog/index.html")

def about(request):
    return render(request,"blog/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        # print(name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'blog/contact.html')

def python(request):
    return render(request,"blog/python.html")

def html(request):
    return render(request,"blog/html.html")

def css(request):
    return render(request,"blog/css.html")

def javascript(request):
    return render(request,"blog/javascript.html")



