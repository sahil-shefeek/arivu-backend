# views.py

from rest_framework import generics
from .models import YouTubeVideo
from .serializers import YouTubeVideoSerializer


class YouTubeVideoListView(generics.ListAPIView):
    queryset = YouTubeVideo.objects.all()
    serializer_class = YouTubeVideoSerializer
