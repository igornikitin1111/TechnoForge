from django.contrib import admin
from . import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('content', 'created', 'published', 'moderation', 'views', 'user')
    list_filter = ('created', 'published', 'moderation')
    search_fields = ('content', 'user')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created', 'published', 'user', 'post')
    list_filter = ('created', 'published')
    search_fields = ('text', 'user')

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)