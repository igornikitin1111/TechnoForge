from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000 )
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=True)
    views = models.PositiveBigIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post by {self.user}"
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

class Comment(MPTTModel):
    text = models.TextField(_("Message"), max_length=1000)
    created = models.DateTimeField(_("Added on"),auto_now_add=True)
    published = models.BooleanField(_("Publish?"), default=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE
        )
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
        )
    def __str__(self):
        return f"{self.text} \n Comment by {self.user}"
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.post.pk})