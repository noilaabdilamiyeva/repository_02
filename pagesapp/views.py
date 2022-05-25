from django.shortcuts import render
from .models import Post

# Create your views here.


def home(req):
    posts = Post.objects.all()[:6]
    return render(req, 'home.html',
                    context={
                        'posts': posts

                    })

def home_detail(req,id):
    posts = Post.objects.get(id=id)
    return render(req, 'home_detail.html',
                context = {
                    'posts': posts

                })

def blog(req):
    posts = Post.objects.all()[7:12]
    return render(req, 'blog.html',
                    context={
                        'posts': posts

                    })


def blog_detail(req, id):
    posts = Post.objects.get(id=id)
    return render(req, 'blog_detail.html',
                    context={
                        'posts': posts

                    })



