from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import models
from . import forms

def post_detail(request, post_id):
    post = models.Post.objects.get(pk=post_id)
    comments = models.Comment.objects.filter(post=post, published=True)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = forms.PostForm()

    return render(request, 'create_post.html', {'form': form})

@login_required
def create_comment(request, post_id):
    post = models.Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = forms.CommentForm()

    return render(request, 'create_comment.html', {'form': form, 'post': post})

