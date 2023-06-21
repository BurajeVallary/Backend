from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField (max_length=32)
    email = models.EmailField()
    contacts = models.CharField (max_length=32)
    location= models.CharField (max_length=32)

    
    def __str__(self):
        return self.name
