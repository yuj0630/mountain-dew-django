from django.db import models
 
# Create your models here.
class blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    hikerid = models.IntegerField(max_length=10)
    pmntnsn = models.DateTimeField(auto_now=True)
    content = models.DateTimeField(max_length=1000)
    postDate = models.DateTimeField(auto_now=True)
    editDate = models.DateTimeField(auto_now=True)
    deleted = models.CharField(max_length=1, choices='N,Y')
