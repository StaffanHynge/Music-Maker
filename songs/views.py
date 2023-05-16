from songs.models import Music
from django.shortcuts import redirect, render


def homePage(request):
    musics = list(Music.objects.all().values())
    return render(request, 'base.html', {
        'musics': musics
    })
