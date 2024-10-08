# Generated by Django 5.0.6 on 2024-08-31 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FGPH', '0004_remove_registereduser_access'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookbook',
            old_name='RegisteredUser',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='cookbook',
            old_name='Recipe',
            new_name='recipe',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipes', to='FGPH.registereduser'),
        ),
    ]
