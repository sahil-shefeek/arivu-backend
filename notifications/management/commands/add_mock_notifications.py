# your_app/management/commands/add_mock_notifications.py

from django.core.management.base import BaseCommand
from notifications.models import Notification
import random
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Add mock notifications to the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating mock notifications...')

        Notification.objects.all().delete()  # Optional: Clear existing notifications

        for _ in range(50):  # Add 50 mock notifications
            title = fake.sentence()
            summary = fake.paragraph(nb_sentences=2)
            content = fake.paragraph(nb_sentences=5)
            source = fake.url()
            Notification.objects.create(
                title=title,
                summary=summary,
                content=content,
                source=source,
            )

        self.stdout.write(self.style.SUCCESS('Successfully added mock notifications'))
