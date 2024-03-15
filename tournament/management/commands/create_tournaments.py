from django.core.management.base import BaseCommand
from tournament.models import Location, Tournament
from main.regions import region_points
import random
from datetime import datetime, timedelta

FAKE_STREET_NAMES = ["Maple Street", "Oak Avenue", "Cedar Lane", "Elm Boulevard", "Pine Road"]
FAKE_CITIES = ["Springfield", "Oakdale", "Maplewood", "Pinehurst", "Willow Creek"]
STATES = {
    'North East': 'New York',
    'South West': 'Arizona',
    'West': 'California',
    'South East': 'Florida',
    'Midwest': 'Illinois',
    'Eastern Canada': 'Ontario',
    'Western Canada': 'British Columbia'
}

TOURNAMENT_NAMES = [
    "Frozen Faceoff",
    "Icebreaker Classic",
    "Slapshot Showdown",
    "Puck Drop Invitational",
    "Breakaway Bash",
    "Hat Trick Tournament",
    "Face-Off Frenzy",
    "Icebound Cup",
    "Rink Rumble",
    "Blizzard Battle",
    "Power Play Palooza",
    "Goalie Gauntlet",
    "Chill Challenge",
    "Frosty Face-off",
    "Icicle Invitational",
    "Snowstorm Shootout",
    "Winter Warzone",
    "Frozen Fury",
    "Frigid Faceoff",
    "Arctic Assault",
]

def generate_fake_address(region):
    fake_street = random.choice(FAKE_STREET_NAMES)
    fake_city = random.choice(FAKE_CITIES)
    state = STATES.get(region)
    number = random.randint(100, 999)
    return f"{number} {fake_street}, {fake_city}, {state}"

class Command(BaseCommand):
    help = 'Creates tournaments for each region with correct coordinates in 2024.'

    def handle(self, *args, **kwargs):
        now = datetime(2024, 1, 1)  # Start of 2024
        for region, coordinates in region_points.items():
            for _ in range(2):  # Add 2 tournaments per region
                # Setting different months for the date (random month in 2024)
                tournament_date = datetime(2024, random.randint(1, 12), random.randint(1, 28))
                tournament_name = random.choice(TOURNAMENT_NAMES)

                location = Location.objects.create(
                    latitude=coordinates[0],
                    longitude=coordinates[1],
                    region=region
                )

                tournament = Tournament.objects.create(
                    name=f"{tournament_name}",
                    date=tournament_date,
                    company='YHT',
                    location=location,
                    address=generate_fake_address(region),
                    draft_status="published"
                )
                self.stdout.write(self.style.SUCCESS(f"Created tournament '{tournament_name}' for region {region}"))