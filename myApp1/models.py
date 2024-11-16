from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    brand_price = models.IntegerField()
    brand_category = models.CharField(max_length=50)
    brand_qty =models.IntegerField()
    brand_img = models.ImageField(upload_to='brands/')
    brand_desc = models.TextField()


def __str__(self):
    return self.brand_name