# Generated by Django 5.0.6 on 2024-09-10 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FGPH', '0045_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
