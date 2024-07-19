from django.urls import path
from .views import home_view,contact_view,about_view,books_view,gallery_view,portfolio_view,blog_view

urlpatterns = [
    path('',home_view,name='home-page'),
    path('about/',about_view,name='about-page'),
    path('contact/',contact_view,name='contact-page'),
    path('books/',books_view,name='books-page'),
    path('gallery/',gallery_view,name='gallery-page'),
    path('portfolio/',portfolio_view,name='portfolio-page'),
    path('blog-since/',blog_view,name='blog-page')
]