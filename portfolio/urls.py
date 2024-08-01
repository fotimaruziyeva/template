from django.urls import path
from .views import (
    home_view, ContactFormView,about_view, books_view,gallery_view,PortfolioListView, blog_view,gallery_single_view,portfolio_single_view
)

urlpatterns = [
    path('', home_view, name='home-page'),
    path('about/', about_view, name='about-page'),
    path('contact/', ContactFormView.as_view(), name='contact-page'),
    path('books/', books_view, name='books-page'),
    path('gallery/', gallery_view, name='gallery-page'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio-page'),
    path('blog-since/', blog_view, name='blog-page'),
    path('gallery-single/', gallery_single_view, name='gallery-single-page'),
     path('portfolio-single/', portfolio_single_view, name='portfolio-single-page'),
]
