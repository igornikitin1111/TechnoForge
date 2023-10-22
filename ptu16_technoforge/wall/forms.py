from django import forms
from .models import Post, Comment
from PIL import Image
from io import BytesIO




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "post_image"]

    def clean_post_image(self):
        post_image = self.cleaned_data.get("post_image")
        if post_image:
            img = Image.open(post_image)
            max_size = (200, 200)
            img.thumbnail(max_size, Image.LANCZOS)

            new_image_io = BytesIO()
            img.save(new_image_io, format="PNG")
            new_image_io.seek(0)

            self.cleaned_data["post_image"] = new_image_io

        return post_image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'published']
