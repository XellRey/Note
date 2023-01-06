from django.shortcuts import render, redirect
from .models import Note
from django.http import Http404, HttpResponseRedirect
from .forms import Note_form

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = Note_form(request.POST)
        if form.is_valid():
            form.save()

    form = Note_form()

    data = {
        'form': form
    }
    return render(request, 'note/index.html', data)


