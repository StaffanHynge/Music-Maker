from songs.models import Music
from django.views import generic
from django.views.generic import CreateView, TemplateView, ListView, DetailView, DeleteView, UpdateView
from django.shortcuts import redirect, render
from .forms import MusicForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class MusicList(ListView):
    model = Music
    template_name = 'songs.html'
    paginate_by = 6
    context_object_name = "music_list"

class AddSong(LoginRequiredMixin, CreateView):
    # Add a song 
    template_name = 'add_song.html'
    model = Music
    form_class = MusicForm
    success_url = '/songs'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddSong, self).form_valid(form)

class HomeView(TemplateView):
    template_name = "home.html"

class SongDetail(DetailView):
    model = Music
    template_name = 'song_detail.html'
    context_object_name = "song"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        song = self.get_object()
        context['pk'] = song.pk
        return context

class DeleteSong(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Music
    success_url = '/songs'
    template_name = 'music_confirm_delete.html' 

    def test_func(self): 
        return self.request.user == self.get_object().user

class EditSong(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'edit_song.html'
    model = Music
    form_class = MusicForm
    success_url = '/songs'

    def test_func(self): 
        return self.request.user == self.get_object().user
