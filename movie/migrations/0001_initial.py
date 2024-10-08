# Generated by Django 4.2.16 on 2024-09-18 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "actor",
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="without_genre", max_length=100)),
            ],
            options={
                "db_table": "genre",
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("year", models.CharField(blank=True, max_length=10, null=True)),
                ("rated", models.CharField(blank=True, max_length=10, null=True)),
                ("released", models.CharField(blank=True, max_length=50, null=True)),
                ("runtime", models.CharField(blank=True, max_length=20, null=True)),
                ("director", models.CharField(blank=True, max_length=255, null=True)),
                ("writer", models.CharField(blank=True, max_length=255, null=True)),
                ("plot", models.TextField(blank=True, null=True)),
                ("language", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("awards", models.TextField(blank=True, null=True)),
                ("poster", models.URLField(blank=True, null=True)),
                ("metascore", models.CharField(blank=True, max_length=10, null=True)),
                ("imdb_rating", models.CharField(blank=True, max_length=10, null=True)),
                ("imdb_votes", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "imdb_id",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
                ("type", models.CharField(blank=True, max_length=50, null=True)),
                ("dvd", models.CharField(blank=True, max_length=50, null=True)),
                ("box_office", models.CharField(blank=True, max_length=50, null=True)),
                ("website", models.URLField(blank=True, null=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        max_length=250,
                        null=True,
                        unique=True,
                        verbose_name="URL",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Published")], default=0
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "actors",
                    models.ManyToManyField(
                        blank=True, related_name="movies", to="movie.actor"
                    ),
                ),
                (
                    "genres",
                    models.ManyToManyField(
                        blank=True, related_name="movies", to="movie.genre"
                    ),
                ),
            ],
            options={
                "verbose_name": "Movie",
                "verbose_name_plural": "Movies",
                "db_table": "movie",
            },
        ),
        migrations.CreateModel(
            name="Production",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "production",
            },
        ),
        migrations.CreateModel(
            name="Rating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("source", models.CharField(max_length=100)),
                ("value", models.CharField(max_length=20)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ratings",
                        to="movie.movie",
                    ),
                ),
            ],
            options={
                "db_table": "rating",
            },
        ),
        migrations.AddField(
            model_name="movie",
            name="production",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="movies",
                to="movie.production",
            ),
        ),
    ]
