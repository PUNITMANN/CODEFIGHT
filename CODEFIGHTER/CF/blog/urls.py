from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="blog"),
    path('index/', views.index, name='INDEX'),
    path('about.html/', views.about, name='ABOUTUS'),
    path('contact.html/', views.contact, name='CONTACTUS'),
    path('blog/python.html/', views.python, name='PYTHON'),
    path('blog/html.html/', views.html, name='HTML'),
    path('blog/css.html/', views.css, name='CSS'),
    path('blog/javascript.html/', views.javascript, name='JAVASCRIPT'),

]