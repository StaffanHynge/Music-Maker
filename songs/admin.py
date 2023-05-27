from django.contrib import admin
from .models import Music
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Music)
class MusicAdmin(SummernoteModelAdmin):
    summernote_fields = 'background'



