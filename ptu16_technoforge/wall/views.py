from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect , get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post, published=True)
    return render(request, 'wall/post_detail.html', {'post': post, 'comments': comments})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm()

    return render(request, 'wall/create_post.html', {'form': form})

@login_required
def create_comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'wall/create_comment.html', {'form': form, 'post': post})

class PostListView(generic.ListView):
    queryset = Post.objects.filter(published=True)
    context_object_name = 'posts'
    model = Post
    paginate_by = 3
    template_name = 'wall/post_list.html'