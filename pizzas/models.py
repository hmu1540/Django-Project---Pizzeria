from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200)

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=CASCADE)
    name = models.CharField(max_length=200)
    
