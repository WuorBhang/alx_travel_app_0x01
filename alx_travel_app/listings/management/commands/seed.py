from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        # Optional: clear existing data
        Listing.objects.all().delete()

        owner, _ = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@example.com'}
        )

        locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Naivasha', 'Diani']
        for i in range(10):
            Listing.objects.create(
                name=f"Cozy Home #{i + 1}",
                description="A lovely place to relax and explore.",
                location=random.choice(locations),
                price_per_night=random.randint(5000, 15000),
                owner=owner
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded listings!"))
