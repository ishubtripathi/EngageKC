# Generated by Django 5.1.1 on 2024-10-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0011_alter_media_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='character_set',
            field=models.CharField(default='marvel', max_length=50),
        ),
    ]
