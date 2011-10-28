from django.db import models

# Create your models here.

class Camera(models.Model):
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    flashStream = models.URLField()
    HLSstream = models.URLField()

    def __unicode__(self):
        return self.city
        return self.address

class Event(models.Model):
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    type = models.CharField(max_length=30)

    def __unicode__(self):
         return self.address
