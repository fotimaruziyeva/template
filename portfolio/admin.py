from django.contrib import admin
from .models import  Contact,Book,Comment,Category,Gallery,Portfolio,Blog
# Register your models here.
admin.site.register((Contact,Book,Comment,Category,Gallery,Portfolio,Blog))