# Generated by Django 4.2.6 on 2023-10-31 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrackApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(to='TrackApp.song'),
        ),
    ]