from django.contrib import admin
from .models import  Contact,Book,Comment,PortfolioCategory,Gallery,Portfolio,Blog,About,Category
from django.utils.html import format_html
admin.site.register((Contact,Comment,PortfolioCategory,Gallery,Portfolio,Blog,About,Category))


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_image', 'pages')
    def image(self,obj):
        return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))