from django.contrib import admin
from traffic.locations.models import Camera, Event

admin.site.register(Camera)
admin.site.register(Event)
