from distutils.log import error
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os
import uuid
import boto3
from .models import Venue, Amenity, Photo
from .forms import CommentForm


def home(request):
    return render(request, 'home.html')

@login_required
def venues_index(request):
   venues = Venue.objects.all()
   return render(request, 'venues/index.html', {'venues': venues})

@login_required
def venues_detail(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    id_list = venue.amenities.all().values_list('id')
    amenities_venue_doesnt_have = Amenity.objects.exclude(id__in=id_list)
    comment_form = CommentForm()
    return render(request, 'venues/detail.html', {
      'comment_form': comment_form,
      'venue': venue,
      'amenities': amenities_venue_doesnt_have
  })

class VenueCreate(LoginRequiredMixin, CreateView):
    model = Venue
    fields = ['name', 'description', 'date']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class VenueUpdate(LoginRequiredMixin, UpdateView):
    model = Venue
    fields = ['description', 'name']

class VenueDelete(LoginRequiredMixin, DeleteView):
    model = Venue
    success_url = '/venues/'

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
  fields = '__all__'

class AmenityDelete(LoginRequiredMixin, DeleteView):
  model = Amenity
  success_url = '/amenities/'

@login_required
def add_photo(request, venue_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, venue_id=venue_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', venue_id=venue_id)

@login_required
def add_comment(request, venue_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.venue_id = venue_id
    # new_comment.user_id = request.user.id
    new_comment.username = request.user.username
    new_comment.save()
  return redirect('detail', venue_id=venue_id)

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