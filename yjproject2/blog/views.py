from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects #쿼리셋 #메소드 #기능을표시
    return render(request, 'home.html' , {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def post(request):
    return render(request, 'post.html')