from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'note/index.html')


def note(request, note_id):
    return HttpResponse("Yours Notes:" % note_id)
