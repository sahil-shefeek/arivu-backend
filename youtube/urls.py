# urls.py

from django.urls import path
from .views import YouTubeVideoListView

urlpatterns = [
    path('', YouTubeVideoListView.as_view(), name='youtube-video-list'),
]