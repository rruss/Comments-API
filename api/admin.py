from django.contrib import admin
from .models import Activity, Comment, Post, UserPage


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'essence_id',
        'essence_type',
        'created_at',
    )
    list_filter = ('created_at',)
    search_fields = ('user',)
    date_hierarchy = 'created_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'text', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ('title',)
    date_hierarchy = 'created_at'


@admin.register(UserPage)
class UserPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ('user',)
    date_hierarchy = 'created_at'
