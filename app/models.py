from django.db import models

class Product(models.Model):
 name = models.CharField(max_length=50)
 product_image = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=None)
 description = models.TextField()
 price = models.IntegerField()
