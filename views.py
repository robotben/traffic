from django.shortcuts import render_to_response
from locations.models import Camera

def index(request):
    return render_to_response('index.html')

def start_map(request, city):
    camera_locations = Camera.objects.filter(city=city)
    return render_to_response('map.html', {'camera_locations': camera_locations})
