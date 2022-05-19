from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

AMENITY_CATEGORY = (
  ('Health', 'Health'),
  ('Food', 'Food'),
  ('Drinks', 'Drinks'),
  ('Misc', 'Misc'),
)


class Amenity(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(
    max_length=19,
    choices=AMENITY_CATEGORY
    )

    def get_absolute_url(self):
     return reverse('amenities_detail', kwargs={'pk': self.id})


class Venue(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('When did you go?')
    amenities = models.ManyToManyField(Amenity)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'venue_id': self.id})

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str___(self):
        return f'Photo for venue_id: {self.venue_id} @ {self.url}'



class Comment(models.Model):
    date = models.DateField('Visit Date')
    content = models.CharField('comment', max_length=200)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)

