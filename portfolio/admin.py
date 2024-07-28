from django.contrib import admin
from .models import  Contact,Book,Comment,Category,Gallery,Portfolio,Blog,About
from django.utils.html import format_html
# Register your models here.
admin.site.register((Contact,Comment,Category,Gallery,Portfolio,Blog,About))

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_image', 'pages')
    def image(self,obj):
        return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))