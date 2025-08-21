from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='bands'),
    path('bands/add/', views.band_create, name='band-create'),
    path('listings/add/', views.listing_create, name='listing_create'),
    path('about-us/', views.about, name='about'),
    path('listings/', views.listings, name='listings'),
    path('contact-us/', views.contact, name='contact'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    
]
