# from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


# Create your views here.

# CBV 방식
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/index.html'

class PostDetail(DetailView):
    model = Post

# FBV 방식
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post': post
#         }
#     )

