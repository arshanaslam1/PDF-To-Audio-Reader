from main.models import PDFAudio
from main.utils import convert_pdf_to_audio
from config.celery import app


@app.task
def generate_audio(obj_id):
    print('audio gen called')
    obj = PDFAudio.objects.get(pk=obj_id)
    text, file_name = convert_pdf_to_audio(obj)
    obj.text = text.strip()
    obj.audio_file = file_name
    print(obj.text, obj.audio_file)
    obj.save()



