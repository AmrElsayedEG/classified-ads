from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import slugify


class Products(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    about = models.TextField()
    categories = models.TextField(choices=(('vehicle','vehicle'),('laptops','laptops'),('mobile','mobile'),('electronics','electronics'),('computer','computer'),('real estate','real estate'),('home appliances','home appliances'),('jobs','jobs')),default='else',blank=False)
    phone = models.CharField(max_length=15)
    img = models.ImageField(upload_to='product_img',blank=True,default='/product_img/default.bmp')
    country = models.TextField(choices=(('Egypt','Egypt'),('USA','USA'),('UAE','UAE')),default='else',blank=False)
    address = models.TextField(max_length=100,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=User)

    def __str__(self):
        return self.title

class Comments(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length = 500)

    def __str__(self):
        return self.product

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.OneToOneField(Products,on_delete=models.CASCADE)