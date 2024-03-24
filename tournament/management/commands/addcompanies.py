from django.core.management.base import BaseCommand
from tournament.models import TournamentCompany

TOURNAMENT_COMPANY_CHOICES = [
    ('I dont know', 'Idk'),
    ('Organized by Club/Rink', 'Organized by Club/Rink'),
    ('Youth Hockey Tournaments', 'YHT'),
    ('CAN/AM', 'CAN/AM'),
    ('Canadian Hockey Enterprises', 'CHE'),
    ('EliteAMSports', 'EAS'),
    ('MyHockey Tournaments', 'MHT'),
    ('OneHockey Tournaments', 'OHT'),
]

class Command(BaseCommand):
    help = 'Adds tournament companies to the database'

    def handle(self, *args, **kwargs):
        for name, abbr in TOURNAMENT_COMPANY_CHOICES:
            TournamentCompany.objects.get_or_create(name=name, abbr=abbr)
        self.stdout.write(self.style.SUCCESS('Tournament companies added successfully'))