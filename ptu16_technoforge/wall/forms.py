from django import forms
from .models import Post, Comment
from PIL import Image


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", 'content', 'post_image']
    def clean_post_image(self):
        post_image = self.cleaned_data.get('post_image')
        if post_image:
            img = Image.open(post_image)
            max_size = (200, 200)
            img.thumbnail(max_size, Image.ANTIALIAS)
            img.save(post_image.path)
        return post_image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'published']
