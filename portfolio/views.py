from django.shortcuts import render
from portfolio.forms import ContactForm
from .models import Gallery,Book,Blog,About
from django.views.generic.edit import FormView
class ContactFormView(FormView):
    template_name="contact.html"
    forms_class=ContactForm
    success_url='/'
def home_view(request):
    return render(request=request,template_name='index.html')

def contact_view(request):
 return render(request=request,template_name='contact.html')

def about_view(request):
     about = About.objects.all()
     context = {
          "about": about,
      }
     return render(request=request,template_name='about.html', context=context)

def books_view(request):
      books = Book.objects.all()
      context = {
          "books": books,
      }
      return render(request=request,template_name='books.html',context=context)

def gallery_view(request):
    gallery = Gallery.objects.all()
    context = {
        "gallery": gallery,
    }
    return render(request, template_name='gallery.html', context=context)

def portfolio_view(request):
 return render(request=request,template_name='portfolio.html')

def blog_view(request):
    blog=Blog.objects.all()
    context ={
        "blog":blog,
    }
    return render(request=request,template_name='blog-masonry.html',context=context)

def gallery_single_view(request):
    gallery = Gallery.objects.all()
    context = {
        "gallery": gallery,
    }
    return render(request=request,template_name='gallery-single.html',context=context)