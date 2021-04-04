from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf.urls import url
from api.views import *

urlpatterns = [
    path('userdetails/', UserDetailsView.as_view(), name="user-details"),
]
