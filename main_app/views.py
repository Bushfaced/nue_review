from distutils.log import error
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# import os
# import uuid
# import boto3
from .models import Venue, Amenity, Photo
# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def venues_index(request):
    # venues.all
    return render(request, 'venues/index.html')

@login_required
def venues_detail(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    id_list = venue.amenities.all().values_list('id')
    amenities_venue_doesnt_have = Amenity.objects.exclude(id__in=id_list)
    return render(request, 'venues/detail.html',
    {'venue': venue,'amenities': amenities_venues_doesnt_have})

class VenueCreate(LoginRequiredMixin, CreateView):
    model = Venue
    fields = ['user', 'date', 'description', 'name', 'amenities']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class VenueUpdate(LoginRequiredMixin, UpdateView):
    model = Venue
    fields = ['description', 'name', 'amenities']

class VenueDelete(LoginRequiredMixin, DeleteView):
    model = Venue
    success_url: '/venues/'

@login_required
def assoc_amenity(request, venue_id, amenity_id):
    Venue.objects.get(id=venue_id).amenities.add(amenity_id)
    return redirect('detail', venue_id=venue_id)

@login_required
def unassoc_amenity(request, venue_id, amenity_id):
    Venue.objects.get(id=venue_id).amenities.remove(amenity_id)
    return redirect('detail', venue_id=venue_id)

class AmenityList(LoginRequiredMixin, ListView):
  model = Amenity

class AmenityDetail(LoginRequiredMixin, DetailView):
  model = Amenity

class AmenityCreate(LoginRequiredMixin, CreateView):
  model = Amenity
  fields = '__all__'

class AmenityUpdate(LoginRequiredMixin, UpdateView):
  model = Amenity
  fields = ['name', 'description', ]

class AmenityDelete(LoginRequiredMixin, DeleteView):
  model = Amenity
  success_url = '/amenities/'







def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign-up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)