from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post

from django.utils.timezone import localdate
from datetime import datetime
from events.models import Event



# Create your views here.

def cad_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/cad_list.html', {'posts': posts})

def cad_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/cad_detail.html', {'post': post})

def cad_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def day():
    day = datetime(localdate().year,localdate().month,localdate().day)
    context = {
        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
    }


def cad_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {
        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
        'form': form
    }

    return render(request, 'blog/post_edit.html', context)