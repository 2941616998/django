from django.db import models

# Create your models here.

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)
    
class Map(models.Model):
    id = models.AutoField(primary_key=True)
    map= models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)