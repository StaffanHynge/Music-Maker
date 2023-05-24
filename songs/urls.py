from . import views
from django.urls import path
from .views import AddSong, MusicList, HomeView, SongDetail

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add_song/", AddSong.as_view(), name="add_song"),
    path("songs", MusicList.as_view(), name="songs"),
    path("<slug:pk>/", SongDetail.as_view(), name="song_detail"),
]