from django.shortcuts import render, redirect , get_object_or_404
from django.utils import timezone
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

def create(request): #입력받은 내용을 데베에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) # redirect: 위에 사항 모두를 처리한 뒤 다음 주소로 이동