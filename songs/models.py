from django.db import models
from django.contrib.auth.models import User
from songs.helpers import get_audio_length
from songs.validators import validate_is_audio


class Music(models.Model):
    user = models.ForeignKey(
        User, related_name='song_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=False, blank=False)
    artist = models.CharField(max_length=500, null=False, blank=False)
    audio_file = models.FileField(
        upload_to='songs/', default='', validators=[validate_is_audio])
    time_length = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0)
    cover_image = models.ImageField(upload_to='music_images/')
   # image_alt = models.CharField(max_length=100, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.time.length:

            audio_length = get_audio_length(self.audio_file)
            self.time_length = audio_length
        return super().save(*args, **kwargs)
