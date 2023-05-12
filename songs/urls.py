
from django.urls import path
from .views import Index
from django.urls import path, include

app_name = 'songs'

urlpatterns = [
    path('', Index.as_view(), name='home'),
]
