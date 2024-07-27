from django.urls import path, include

urlpatterns = [
    path('query/', include('client.urls')),
    path('notifications/', include('notifications.urls')),

    path('youtube-videos/', include('youtube.urls')),
]