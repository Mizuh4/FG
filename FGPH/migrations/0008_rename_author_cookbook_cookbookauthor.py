# Generated by Django 5.0.6 on 2024-09-03 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FGPH', '0007_cookbook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookbook',
            old_name='author',
            new_name='cookbookAuthor',
        ),
    ]
