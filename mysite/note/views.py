from django.shortcuts import render, redirect
from .models import Note
from django.http import Http404, HttpResponse
from .forms import Note_form
from django.views.generic import DeleteView, UpdateView

# Create your views here.


def index(request):
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
    return render(request, 'note/index.html', data)


def note(request, note_id):
    n_list = Note.objects.all()
    try:
        n = Note.objects.get(id=note_id)
    except:
        raise Http404("Page not found")

    form = Note_form()

    data = {
        'note': n,
        'n_list': n_list
    }
    return render(request, 'note/note.html', data)


class edit(UpdateView):
    model = Note
    template_name = 'note/n_edit.html'
    form_class = Note_form


def delete(request, note_id, ):
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


