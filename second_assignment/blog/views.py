from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

def blog(request):
    blogs = Blog.objects 
    blog_list = Blog.objects.all() #블로그 모든 글 대상
    paginator = Paginator(blog_list, 3) #객체들을 개수대로 한 페이지로 자르기
    page = request.GET.get('page') #request 페이지를 변수에 담기
    posts = paginator.get_page(page) #request된 페이지를 얻어온 뒤 return
    return render(request, 'blog/blog.html', {'blogs': blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def edit(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)

    if request.method=="POST":
        blog.title = request.POST.get('title')
        blog.body = request.POST.get('body')
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/' + str(blog.id))

    return render(request, 'blog/edit.html', {'blog': blog})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('home')