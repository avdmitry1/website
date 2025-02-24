# Generated by Django 5.1.4 on 2025-02-21 15:25

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_event_date_alter_socialmedialink_url_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date'], 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='socialmedialink',
            options={'ordering': [django.db.models.functions.text.Lower('platform')], 'verbose_name': 'Social Media Link', 'verbose_name_plural': 'Social Media Links'},
        ),
        migrations.RemoveIndex(
            model_name='event',
            name='event_date_index',
        ),
        migrations.AlterField(
            model_name='podcast',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='podcasts/'),
        ),
        migrations.AlterField(
            model_name='release',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AddIndex(
            model_name='artist',
            index=models.Index(fields=['name'], name='artist_name_idx'),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['date'], name='event_date_index'),
        ),
    ]
