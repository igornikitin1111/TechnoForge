from typing import Any
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect , get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.contrib import messages
from taggit.models import Tag
from django.db.models import Count

@login_required
def create_post(request ):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm()

    return render(request, 'wall/create_post.html', {'form': form})

@login_required
def create_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment succesfully added')
            return redirect('post_detail', post_pk=post_pk)
    else:
        form = CommentForm()

    return render(request, 'wall/create_comment.html', {'form': form, 'post': post})

def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.views += 1
    post.save()
    comments = Comment.objects.filter(post=post, published=True)
    return render(request, 'wall/post_detail.html', {'post': post, 'comments': comments})

class PostListView(generic.ListView):
    queryset = Post.objects.filter(published=True)
    context_object_name = 'posts'
    model = Post
    paginate_by = 3
    template_name = 'wall/post_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        tag_slug = self.request.GET.get('tag_slug')
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = super().get_queryset().filter(tags__in=[tag])
        else:
            queryset = super().get_queryset()
        
        if tag:
            post_tags_ids = tag.values_list('id', flat=True)
            similar_posts = Post.published(tags__in=post_tags_ids).exclude(id=self.object.id)
            similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-created')[:4]
            queryset = queryset.annotate(similar_posts=similar_posts)
            
        return queryset