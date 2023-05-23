from songs.models import Music
from django.views import generic
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from .forms import MusicForm
from django.contrib.auth.mixins import LoginRequiredMixin

class MusicList(generic.ListView):
    model = Music
    queryset = Music.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 6

class AddSong(LoginRequiredMixin, CreateView):
    # Add a song 
    template_name = 'add_song.html'
    model = Music
    form_class = MusicForm
    success_url = '/add_song/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddSong, self).form.valid(form)