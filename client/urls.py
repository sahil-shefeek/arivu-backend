from django.urls import path

from client.views import QueryPromptAPIView

urlpatterns = [
    path('', QueryPromptAPIView.as_view(), name='query-prompt'),
]
