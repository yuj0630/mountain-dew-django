from django.db import models

# Create your models here.
class hiker(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    PW = models.CharField(max_length=20, null=False)
    firstName = models.CharField(max_length=20, null=False)
    lastName = models.CharField(max_length=20, null=False)
    SSN = models.CharField(max_length=14, null=False, unique=True)
    age = models.IntegerField(max_length=2)
    sex = models.CharField(max_length=1, choices='M,F')
    phone = models.CharField(max_length=13, unique=True)