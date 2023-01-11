from django.shortcuts import render
from .models import Note
from django.http import Http404
from .forms import Note_form
from django.views.generic import UpdateView
from django.db.models import Q
# Create your views here.


def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(note_title__icontains=q) | Q(note_text__icontains=q))
        n_list = Note.objects.filter(search)
    else:
        n_list = Note.objects.all()
    if request.method == 'POST':
        form = Note_form(request.POST)
        if form.is_valid():
            form.save()

    form = Note_form()

    data = {
        'form': form,
        'n_list': n_list,
    }
    return render(request, 'note/index.html', data)


def note(request, note_id):
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(note_title__icontains=q) | Q(note_text__icontains=q))
        n_list = Note.objects.filter(search)
    else:
        n_list = Note.objects.all()

    try:
        n = Note.objects.get(id=note_id)

    except n.DoesNotExist:
        raise Http404("Page not found")

    data = {
        'note': n,
        'n_list': n_list
    }
    return render(request, 'note/note.html', data)


class edit(UpdateView):
    model = Note
    template_name = 'note/n_edit.html'
    form_class = Note_form


def delete(request, note_id):
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(note_title__icontains=q) | Q(note_text__icontains=q))
        n_list = Note.objects.filter(search)
    else:
        n_list = Note.objects.all()

    if request.method == 'POST':
        form = Note_form(request.POST)
        if form.is_valid():
            form.save()

    form = Note_form()
    data = {
        'form': form,
        'n_list': n_list
    }
    try:
        n = Note.objects.get(id=note_id)
        n.delete()
    except:
        print("")

    return render(request, 'note/index.html', data)
