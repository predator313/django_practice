"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

# from .. import pre
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.pre,name='pre'),
    path('about',views.about,name='about'),
    path('home',views.home,name='home'),
    path('markup',views.markup,name='markup'),
    path('predator',views.predator,name='predator'),
    # path('capi',views.capi,name='capi'),
    path('analyze',views.analyze,name='analyze'),
    path('aamir',views.aamir,name='aamir')
    # path('CAPATALIZE',views.CAPATALIZE,name='CAPATALIZE')
    # path('/about',pre.fun,name='fun')
]
