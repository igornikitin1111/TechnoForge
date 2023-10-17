from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',  'created', 'published', 'moderation', 'views', 'user')
    list_filter = ('created', 'published', 'moderation')
    search_fields = ('content', 'user')

class CommentAdmin(MPTTModelAdmin):
    list_display = ('text', 'created', 'published', 'user')
    list_filter = ('created', 'published')
    search_fields = ('text', 'user')

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, MPTTModelAdmin)