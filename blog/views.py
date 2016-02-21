from django.shortcuts import render
from .models import Post, Author

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')
    
def contact(request):
    return render(request, 'blog/contact.html')
    
def post_list(request):
    p = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': p})
    
def post_detail(request, post_id):
    p = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': p})

def author_list(request):
    a = Author.objects.all()
    return render(request, 'blog/author_list.html', {'authors': a})
    
def author_detail(request, author_id):
    a = Author.objects.get(id=author_id)
    return render(request, 'blog/author_detail.html', {'author': a})