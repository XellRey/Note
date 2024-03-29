from django.db import models

# Create your models here.


class Note(models.Model):
    note_title = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
    note_text = models.CharField(max_length=3000)

    def __str__(self):
        return self.note_title

    def get_absolute_url(self):
        return f'/{self.id}'