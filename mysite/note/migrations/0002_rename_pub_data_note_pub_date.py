# Generated by Django 4.1.5 on 2023-01-04 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
