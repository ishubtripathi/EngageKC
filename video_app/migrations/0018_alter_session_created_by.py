# Generated by Django 5.0.6 on 2024-07-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("video_app", "0017_session_created_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="session",
            name="created_by",
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
