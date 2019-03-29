from django.contrib import admin

# Register your models here.
from ads.models import Products, Comments, Favorites

admin.site.register(Products)
admin.site.register(Comments)
admin.site.register(Favorites)
