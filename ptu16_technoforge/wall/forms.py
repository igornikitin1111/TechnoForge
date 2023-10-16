from django import forms
from .models import Post, Comment


class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ['content']

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ['text', 'published']
