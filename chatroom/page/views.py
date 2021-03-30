from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from rest_framework import generics
from page.serializers import *
#from django.contrib.auth.decorators import login_required

class PageSerializerView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

def page(request):
    posts = Post.objects.all()
    return render(request, 'page/page.html', {'posts': posts})

def message(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('message')
    else:
        form = PostForm()
    return render(request, 'page/message.html', {'form': form, 'posts': posts})

def REDIRECT(request):
    return redirect('message')
