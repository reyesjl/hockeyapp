from django.core.management.base import BaseCommand
from tournament.models import Location, Tournament
from main.regions import region_points

class Command(BaseCommand):
    help = 'Creates a tournament for each region with correct coordinates.'

    def handle(self, *args, **kwargs):
        for region, coordinates in region_points.items():
            # Check if a tournament for this region already exists
            if Tournament.objects.filter(location__region=region).exists():
                self.stdout.write(self.style.WARNING(f"Tournament for region {region} already exists. Skipping..."))
                continue

            location = Location.objects.create(
                latitude=coordinates[0],
                longitude=coordinates[1],
                region=region
            )

            tournament = Tournament.objects.create(
                name=f"Tournament in {region}",
                location=location,
                address="",
                draft_status="published"
            )
            self.stdout.write(self.style.SUCCESS(f"Created tournament for region {region}"))
