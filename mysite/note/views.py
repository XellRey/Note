from django.shortcuts import render
from .models import Note
from django.http import Http404, HttpResponseRedirect
# Create your views here.


def index(request):
    latest_note = Note.objects.order_by('-pub_date')
    return render(request, 'note/index.html', {'latest_note': latest_note})

def detail(request, note_id):
    try:
        n = Note.objects.get(id = note_id)
    except:
        raise Http404("Note not found")

    return render(request, 'note/detail.html', {'note': n})
