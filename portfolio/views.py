from django.shortcuts import render
from django.contrib import messages
from portfolio.forms import ContactForm
from .models import Gallery, Book, Blog, About,Portfolio,PortfolioCategory,Category
from django.views.generic.edit import FormView
from .bot import send_message
from django.views.generic.list import ListView

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        content = form.cleaned_data.get('content')
        text = f"Name: {name}\nEmail: {email}\nContent: {content}"
        send_message(text)
        
        # form.save() o'rniga ma'lumotlarni saqlashni qo'shing agar kerak bo'lsa
        # example: 
        # form.instance.save()

        return super().form_valid(form)
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
class PortfolioListView(ListView):
    model = Portfolio
    # paginate_by = 100  # if pagination is desired
    context_object_name = 'portfolios'
    template_name = "portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = PortfolioCategory.objects.all()
        return context

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
def portfolio_single_view(request):
    return render(request=request,template_name='portfolio-single.html')