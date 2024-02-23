from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Info

# Create your views here.

class IndexView(ListView):
  model = Info
  template_name = 'index.html'
  
class InfoCreateView(TemplateView):
  model = Info
  template_name = 'info_create.html'
