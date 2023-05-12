from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Music

class Index(TemplateView):
    music = Music.objects.all()
    template_name = 'home/index.html'