from django.core.management.base import BaseCommand
from locations.models import MajorCity
import os

class Command(BaseCommand):
    help = 'Load major cities from text file.'

    def handle(self, *args, **options):
        # Path to the file:
        file_path = 'cleaned_cities.txt'

        # Open the file and read the city state pairs
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Parse the lines and create MajorCity objects
        for i in range(0, len(lines), 2):
            city_name = lines[i].strip()
            state = lines[i+1].strip()

             # Create and save MajorCity object
            MajorCity.objects.create(cityname=city_name, state=state)

        self.stdout.write(self.style.SUCCESS('Major cities loaded successfully'))
