# management/commands/add_mock_youtube_videos.py

from django.core.management.base import BaseCommand

from youtube.models import YouTubeVideo


class Command(BaseCommand):
    help = 'Add mock YouTube videos to the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating mock YouTube videos...')

        YouTubeVideo.objects.all().delete()  # Optional: Clear existing videos

        videos = [
            {
                'title': 'Empowering Talk 1',
                'description': 'An inspiring talk on empowerment.',
                'video_url': 'https://www.youtube.com/watch?v=example1'
            },
            {
                'title': 'Empowering Talk 2',
                'description': 'Another inspiring talk on empowerment.',
                'video_url': 'https://www.youtube.com/watch?v=example2'
            },
            # Add more video details here
        ]

        for video in videos:
            YouTubeVideo.objects.create(**video)

        self.stdout.write(self.style.SUCCESS('Successfully added mock YouTube videos'))