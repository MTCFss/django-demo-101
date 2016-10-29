from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Author

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def contact(request):
    return render(request, 'blog/contact.html')

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class AuthorList(ListView):
    model = Author

class AuthorDetail(DetailView):
    model = Author
