from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from accounts.models import User
from main.utils import convert_pdf_to_audio

AUDIO_VOICES = (
    ( 0, 'Male'),
    ( 1, 'Female')
)


class PDFAudio(models.Model):

    class AudioVoice(models.IntegerChoices):
        Male = 0
        Female = 1

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    text = models.TextField(blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs', validators=[FileExtensionValidator(['pdf'])])
    audio_file = models.FileField(upload_to='recs', blank=True, null=True)
    audio_rate = models.IntegerField(validators=[MaxValueValidator(300, "audio_rate would be maximum 175"),
                                                 MinValueValidator(100, "audio_rate would be minimum 75")],
                                     blank=False,
                                     null=False,
                                     default=200
                                     )
    volume_level = models.DecimalField(validators=[MaxValueValidator(1.0, "Volume would be maximum 1.0"),
                                                   MinValueValidator(0.1, "Volume would be minimum 0.1")],
                                       decimal_places=1,
                                       max_digits=2,
                                       blank=False,
                                       null=False,
                                       default=1.0
                                       )
    audio_voice = models.IntegerField(blank=False,
                                   null=False,
                                   choices=AudioVoice.choices,
                                   default=1
                                   )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.owner

    def get_absolute_url(self):
        return reverse('main:pdf-home')

    def audio_url(self):
        try:
            return self.audio_file.url
        except:
            return None

