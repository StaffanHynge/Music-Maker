from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Music


class MusicForm(forms.ModelForm):

    class Meta:
        model = Music
        fields = ['title', 'artist', 'link', 'background', 'image']

        background = forms.CharField(widget=RichTextWidget())

        widget = {
            "background": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Song Title",
            "artist": "Name of the Artist",
            "image": "Cover Image",
            "link": "Post a Link",
            "background": "Story of the song"
        }
        