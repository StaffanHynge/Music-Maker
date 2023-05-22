from songs.models import Music
from django.views import generic
from django.shortcuts import redirect, render

class MusicList(generic.ListView):
    model = Music
    queryset = Music.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 6
