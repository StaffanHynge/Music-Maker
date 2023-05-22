from . import views
from django.urls import path

urlpatterns = [
    path("", views.MusicList.as_view(), name="home"),
]