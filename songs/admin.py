from django.contrib import admin
from .models import Music, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Music)
class MusicAdmin(SummernoteModelAdmin):
    summernote_fields = 'background'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')



