from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # name is blog-home because we want to do a reverse look-up and having a generic name may cause a collision with "home" in another application.
    # path('', admin.site.urls, name='blog-home-2'),
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about')
]
