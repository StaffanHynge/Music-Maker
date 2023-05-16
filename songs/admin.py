from django.contrib import admin
from .models import Music


class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'artist',
                    'audio_file', 'time_length', 'cover_image')


admin.site.register(Music, MusicAdmin)
