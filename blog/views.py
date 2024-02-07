from django.shortcuts import render, get_list_or_404
from django.views import View
from django.http import Http404
from .models import Post
import datetime
from django.core.paginator import Paginator

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
        paginator = Paginator(posts, 2)
        page_number = request.GET.get('page', 1)
        posts = paginator.page(page_number)
        context = {
            'posts': posts
        }
        return render(request, './blog/list.html', context)


class PostDetaileView(View):
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
            context = {
                'post': post,
                'date': datetime.datetime.now()
            }
            return render(request, './blog/detail.html', context)
        except Post.DoesNotExist:
            return Http404("404 Does Not Exist")
