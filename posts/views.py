
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.contrib.auth.models import User
from .models import Post
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
import datetime


def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        raise Http404("Пост не найден!")
    if request.META.get('HTTP_REFERER') == 'http://127.0.0.1:8000/news' + str(post_id) + '/':
        pass
    else:
        request.session['return_path'] = request.META.get('HTTP_REFERER', '/')

    return render(request, 'posts/post.html', {"post": post})


def news(request):
    posts = Post.objects.all().exclude(author=request.user).order_by("-pubdate")
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 20)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'posts/news.html', {'posts': post_list})


def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user;
            post.pubdate = datetime.datetime.now()
            post.save()
            form = PostForm()
            messages.success(request, "Successfully created")

    return render(request, 'posts/form.html', {'form': form})