from django import forms
from .import models


class PostForm(forms.Form):
    class Meta:
        model = models.Post
        fields = ['content']

class CommentForm(forms.Form, models):
    class Meta:
        model = models.Comment
        fields = ['text', 'published']
