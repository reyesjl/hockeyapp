from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender='tournaments.Tournament')
def create_tournament_metadata(sender, instance, created, **kwargs):
    if created:
        from .models import TournamentMetadata  # Import inside the function
        logger.info(f"Tournament {instance} created. Creating TournamentMetadata.")
        TournamentMetadata.objects.create(tournament=instance)