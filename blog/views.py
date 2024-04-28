from django.shortcuts import render
from blog.models import Post
# Create your views here.

def home (request):
    posts = Post.objects.all()
    return render (request,'layout.html', {'posts': posts})


def post(request, post_id):
    posts = Post.objects.get(pk=post_id)
    return render(request, 'layout.html', {'post': post})
