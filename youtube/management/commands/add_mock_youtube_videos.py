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
                'video_url': 'https://youtu.be/AKXatsxB3Dc?si=LS6mnE6ttSjKpxjA'
            },
            {
                'title': 'Empowering Talk 2',
                'description': 'Another inspiring talk on empowerment.',
                'video_url': 'https://youtu.be/LyAMwvILdlM?si=6mOYXb8rO8bkvvO2'
            },

            {
                'title': 'Empowering Talk 1',
                'description': 'An inspiring talk on empowerment.',
                'video_url': 'https://youtu.be/59oH-GbnK44?si=02PvpCh3paduEHJk'
            },
            {
                'title': 'Empowering Talk 2',
                'description': 'Another inspiring talk on empowerment.',
            },
            # Add more video details here
        ]

        for video in videos:
            YouTubeVideo.objects.create(**video)

        self.stdout.write(self.style.SUCCESS('Successfully added mock YouTube videos'))