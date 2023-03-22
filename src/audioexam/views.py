from django.shortcuts import redirect, render
from django.views import View
from audioexam.models import Audio
from .models import Document

def create_document(request):
    if request.method == 'POST':
        name = request.POST['title']
        text = request.POST['text']
        document = Document(name=name, text=text)
        document.save()
        return redirect('main')
    return render(request, 'base.html')
 
class AudioList(View):

    def get(self, request):
        audio = Audio.objects.all()
        return render(request, "main.html", {"audio": audio})