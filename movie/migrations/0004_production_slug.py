# Generated by Django 4.2.16 on 2024-09-19 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0003_actor_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="production",
            name="slug",
            field=models.SlugField(blank=True, max_length=270, null=True, unique=True),
        ),
    ]
