from django.db import models
from django.urls import reverse

# Create your models here.


class Note(models.Model):
    note_title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date create')
    note_text = models.CharField(max_length=3000)

    def __str__(self):
        return self.note_title

