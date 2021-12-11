from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.json import CaseInsensitiveMixin

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images',blank=True)
    
    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
