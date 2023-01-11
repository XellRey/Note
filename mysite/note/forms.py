import datetime

from .models import Note
from django.forms import ModelForm, TextInput, Textarea


class Note_form(ModelForm):
    class Meta:
        model = Note
        fields = ['note_title', 'note_text']
        pub_date = datetime.datetime.now()
        widgets = {
            "note_title": TextInput(attrs={
                'class': 'n_input',
                'placeholder': '           Name of the note...',
                'style': 'margin-bottom: 20px',



            }),
            "note_text": Textarea(attrs={
                'class': 'n_text',

            }),

        }
