from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import PDFAudio
from main.tasks import generate_audio


@receiver(post_save, sender=PDFAudio)
def profile_create(sender, instance, created, **kwargs):
    if created:
        generate_audio.delay(instance.id)
