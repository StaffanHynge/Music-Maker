from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


STATUS = ((0, "Draft"), (1, "Published"))


class Music(models.Model):
    user = models.ForeignKey(
        User, related_name='song_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=False, blank=False)
    artist = models.CharField(max_length=500, null=False, blank=False)
    link = models.CharField(max_length=500, null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    background = RichTextField(max_length=500, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    image = ResizedImageField(
        size=[400, None], quality=75, upload_to='songs/', force_format='WEBP',
        blank=False, null=False, default='/default_image.jpg'
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

