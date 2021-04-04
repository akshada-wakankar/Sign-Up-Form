from django.db import models
import datetime
# Create your models here.


class UserDetails(models.Model):
    fullname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.fullname)
