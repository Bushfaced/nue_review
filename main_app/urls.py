from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('venues/', views.venues_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),   
    path('venues/<int:venue_id>/', views.venues_detail, name='detail'),
    path('venues/create/', views.VenueCreate.as_view(), name='venues_create'),
    path('venues/<int:pk>/update/', views.VenueUpdate.as_view(), name='venues_update'),
    path('venues/<int:pk>/delete/', views.VenueDelete.as_view(), name='venues_delete'),
    path('venues/<int:venue_id>/', views.venues_detail, name='detail'),
    path('amenities/',views.AmenityList.as_view(),name='amenities_index'),
    path('amenities/<int:pk>/', views.AmenityDetail.as_view(), name='amenities_detail'),
    path('amenities/create/', views.AmenityCreate.as_view(), name='amenities_create'),
    path('amenities/<int:pk>/update/', views.AmenityUpdate.as_view(), name='amenities_update'),
    path('amenities/<int:pk>/delete/', views.AmenityDelete.as_view(), name='amenities_delete'),
    path('amenities/<int:venue_id>/assoc_amenity/<int:amenity_id>/', views.assoc_amenity, name='assoc_amenity'),
    path('amenities/<int:venue_id>/unassoc_amenity/<int:amenity_id>/', views.unassoc_amenity, name='unassoc_amenity'),
    path('venues/<int:venue_id>/add_photo/', views.add_photo, name='add_photo'),
]