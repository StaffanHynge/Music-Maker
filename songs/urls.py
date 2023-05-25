from . import views
from django.urls import path
from .views import AddSong, MusicList, HomeView, SongDetail, DeleteSong, EditSong

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add_song/", AddSong.as_view(), name="add_song"),
    path("songs", MusicList.as_view(), name="songs"),
    path("<slug:pk>/", SongDetail.as_view(), name="song_detail"),
    path("delete/<slug:pk>/", DeleteSong.as_view(), name="delete_song"),
    path("edit/<slug:pk>/", EditSong.as_view(), name="edit_song"),
]