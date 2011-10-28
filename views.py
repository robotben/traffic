from django.shortcuts import render_to_response
from googlemaps import GoogleMaps
#from locations.models import Cameras

def index(request):
    return render_to_response('index.html')

def start_map(request, city):
    gmaps = GoogleMaps("ABQIAAAAFpUDyAf-ZSy4XU-hkz96mhQ3JxWYRuPyN-Z_fedsvk4GzBcwohQJDKgVleWBnjm8QmuXPLoz1oGDMw")
    start = gmaps.address_to_latlng(city)    
    return render_to_response('map.html', {'latlng': start})

def test_page(request, something):
    return render_to_response('test.html', {'something': something})
