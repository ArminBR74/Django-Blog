from django.shortcuts import render
from django.http import Http404
from django.views import View
from .models import Post
# Create your views here.


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, './index.html', context)


class PostListView(View):
    def get(self, request):
        posts = posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, './blog/list.html', context)


class PostDetaileView(View):
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
            context = {
                'post': post
            }
            return render(request, '.blog/detail.html', context)
        except:
            return Http404("404 Does Not Exist")
