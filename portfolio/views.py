from django.shortcuts import render
from .models import BlogPost
def home_view(request):
    blog=BlogPost.objects.all()
    context={
        'blog':blog
    }
    return render(request=request,template_name='index.html',context=context)
def contact_view(request):
 return render(request=request,template_name='contact.html')
def about_view(request):
 return render(request=request,template_name='about.html')
def books_view(request):
 return render(request=request,template_name='books.html')
def gallery_view(request):
 return render(request=request,template_name='gallery.html')
def portfolio_view(request):
 return render(request=request,template_name='portfolio.html')
def blog_view(request):
 return render(request=request,template_name='blog-single.html')