from distutils.log import error
from django.shortcuts import render, redirect
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# import os
# import uuid
# import boto3
# from .models import MODELS HERE
\

# Create your views here.

def home(request):
    return render(request, 'home.html')

def venues_index(request):
    # venues.all
    return render(request, 'venues/index.html')
