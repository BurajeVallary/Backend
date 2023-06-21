from django.db import models

# Create your models here.


class addCart(models.Model):
    quantity= models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    shipping_price =  models.DecimalField(max_digits=6,decimal_places=2)
    Payment_method = models.CharField (max_length=32)
    def __str__(self):
     return self.Payment_method
