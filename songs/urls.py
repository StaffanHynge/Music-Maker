
from songs.views import  homePage
from django.urls import path

app_name = 'songs'

urlpatterns = [
    path('', homePage, name='home_page'),

]




