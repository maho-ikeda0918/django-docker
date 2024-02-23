from django.urls import path
from .views import IndexView, InfoCreateView

app_name = 'info'

urlpatterns = [
  path("", IndexView.as_view(), name="index"),
  path('info_create/', InfoCreateView.as_view(), name='info_create')
]