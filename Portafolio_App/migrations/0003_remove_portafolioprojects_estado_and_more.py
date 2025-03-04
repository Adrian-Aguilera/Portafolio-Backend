# Generated by Django 5.1.4 on 2024-12-17 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio_App', '0002_statusproject_tecnologies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portafolioprojects',
            name='Estado',
        ),
        migrations.RemoveField(
            model_name='portafolioprojects',
            name='technologies',
        ),
        migrations.AddField(
            model_name='portafolioprojects',
            name='Estado',
            field=models.ManyToManyField(default=None, to='Portafolio_App.statusproject'),
        ),
        migrations.AddField(
            model_name='portafolioprojects',
            name='technologies',
            field=models.ManyToManyField(default=None, to='Portafolio_App.tecnologies'),
        ),
    ]
