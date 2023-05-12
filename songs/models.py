from django.db import models
from django.contrib.auth.models import User


class Music(models.Model):
    user = models.ForeignKey(
        User, related_name='song_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=False, blank=False)
    artist = models.CharField(max_length=500, null=False, blank=False)
    audio_file = models.FileField(
        upload_to='songs/', default='')
    time_length = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0)
    cover_image = models.ImageField(upload_to='music_images/')

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
