from django.urls import path

from main_app.models import Amenity
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('venues/', views.venues_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('venues/<int:venue_id>/', views.venues_detail, name='detail'),
    path('amenities/',views.AmenityList.as_view(),name='amenities_index'),
    path('amenities/<int:pk>/', views.AmenityDetail.as_view(), name='amenities_detail'),
    path('amenities/create/', views.AmenityCreate.as_view(), name='amenities_create'),
    path('amenities/<int:pk>/update/', views.AmenityUpdate.as_view(), name='amenities_update'),
    path('amenities/<int:pk>/delete/', views.AmenityDelete.as_view(), name='amenities_delete'),
]