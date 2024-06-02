# Generated by Django 5.0.2 on 2024-06-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_movie_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='app/videos/movies/movie_files/'),
        ),
    ]