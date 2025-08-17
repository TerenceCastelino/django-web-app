from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

from django.shortcuts import render
from .models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    items = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': items})

def contact_us(request):
    return render(request, 'listings/contact.html')
