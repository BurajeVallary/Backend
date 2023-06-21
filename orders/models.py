from django.db import models

# Create your models here.
class orders(models.Model):
    name = models.CharField (max_length=32)
    quantity= models.PositiveBigIntegerField()
    total = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name
