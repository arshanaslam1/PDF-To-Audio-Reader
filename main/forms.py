from django import forms
from django.core.validators import FileExtensionValidator
from main.models import PDFAudio


class CreatePDFForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    pdf = forms.FileField(validators=[FileExtensionValidator(['pdf'])], widget=forms.FileInput(attrs={"accept":"application/pdf"}))

    class Meta:
        model = PDFAudio
        fields = ('pdf', 'audio_rate', 'volume_level',
                  'audio_voice')
