from django.shortcuts import redirect, render
from django.views import View
from audioexam.models import Audio
from .models import Document
import os
from gtts import gTTS
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from config.settings import MEDIA_ROOT, MEDIA_URL

def create_audio_file(name, text):
    audio_file_path = 'audioexam\\audio_files\\' + name[:14] + '.mp3'
    audio_file_full_path = os.path.join(os.getcwd(), audio_file_path)
    print(audio_file_full_path, MEDIA_URL, MEDIA_ROOT)
    if not os.path.exists(audio_file_full_path):
        tts = gTTS(text=text, lang='ru')
        tts.save(audio_file_full_path)
    return audio_file_path

def create_document(request):
    if request.method == 'POST':
        name = request.POST['title']
        text = request.POST['text']
        audio_file = create_audio_file(name, text)
        document = Document(name=name, text=text)
        document.save()
        audio = Audio(document=document, audio_file=audio_file)
        audio.save()
        return redirect('main')
    return render(request, 'base.html')

class AudioList(View):

    def get(self, request):
        audio = Audio.objects.all()
        return render(request, "main.html", {"audio": audio})