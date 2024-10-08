# Generated by Django 5.0.6 on 2024-09-08 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FGPH', '0025_region_acronym'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='acronym',
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(choices=[('RegionI', 'Ilocos Region'), ('RegionII', 'Cagayan Valley'), ('RegionIII', 'Central Luzon'), ('RegionIV‑A', 'CALABARZON'), ('MIMAROPA', 'MIMAROPA Region'), ('RegionV', 'Bicol Region'), ('CAR', 'Cordillera Administrative Region'), ('NCR', 'National Capital Region')], max_length=64, null=True),
        ),
    ]
