from http.client import HTTPResponse
from django.shortcuts import render
from blog.models import Post

# 무조건 request
# "hello" vs. """hello""" : 후자는 여러줄, 주석처리는 아예 보이지 않는 거고 docstring 이건 보임 !




def index(request):
    """포스팅 목록 페이지를 HTML을 반환""" 
    post_qs = Post.objects.all().order_by("-pk")
    return render(request, "blog/index.html", {
        "post_list":post_qs,
        })



def post_detail(request, pk):
    """특정 pk 포스팅 페이지 HTML을 반환"""
    post = Post.objects.get(pk=pk)
    return render(request, "blog/post_detail.html", {
        "post":post,
    })
