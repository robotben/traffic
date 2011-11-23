from django.db import models
from googlemaps import GoogleMaps

# Create your models here.

class Camera(models.Model):
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    flashStream = models.URLField()
    HLSstream = models.URLField()

    def __unicode__(self):
        return self.city
        return self.address
    
    def cam_latlng(self):
        gmaps = GoogleMaps("ABQIAAAAFpUDyAf-ZSy4XU-hkz96mhQ3JxWYRuPyN-Z_fedsvk4GzBcwohQJDKgVleWBnjm8QmuXPLoz1oGDMw")
        cam_latlng = gmaps.address_to_latlng(self.address)
        return cam_latlng

    def city_latlng(self):
        gmaps = GoogleMaps("ABQIAAAAFpUDyAf-ZSy4XU-hkz96mhQ3JxWYRuPyN-Z_fedsvk4GzBcwohQJDKgVleWBnjm8QmuXPLoz1oGDMw")
        city_latlng = gmaps.address_to_latlng(self.city)
        return city_latlng

    def replace_city_spaces(self):
        city_no_spaces = self.city.replace(" ", "_")
        return city_no_spaces

    def replace_address_spaces(self):
        address_no_spaces = self.address.replace(" ", "_")
        return address_no_spaces

class Event(models.Model):
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    type = models.CharField(max_length=30)

    def __unicode__(self):
         return self.address
