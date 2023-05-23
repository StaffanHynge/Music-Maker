from . import views
from django.urls import path
from .views import AddSong

urlpatterns = [
    path("", views.MusicList.as_view(), name="home"),
    path("add_song/", AddSong.as_view(), name="add_song")
]