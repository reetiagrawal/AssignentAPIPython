from django.db import models

# Create your models here.
class User(models.Model):
    text = models.CharField(max_length=25)
    #lastname = models.CharField(max_length=25)
    #email = models.CharField(max_length=50)
