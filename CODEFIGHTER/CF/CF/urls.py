from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
path('admin/', admin.site.urls),
    path('', views.index, name='Home'),
    path('blog/', include('blog.urls')),
    path('blog/python.html/', views.python, name='PYTHON'),
    path('blog/html.html/', views.html, name='HTML'),
    path('blog/css.html/', views.css, name='CSS'),
    path('blog/javascript.html/', views.javascript, name='JAVASCRIPT'),

]