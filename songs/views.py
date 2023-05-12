from django.views.generic import TemplateView
from django.shortcuts import render

class Index(TemplateView):
    template_name = 'home/index.html'