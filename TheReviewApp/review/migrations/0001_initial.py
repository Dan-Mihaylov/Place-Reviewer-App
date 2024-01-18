# Generated by Django 5.0.1 on 2024-01-18 15:04

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('photo', models.URLField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('stars', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('comment', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('helpful_count', models.IntegerField(default=0)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='review.place')),
            ],
        ),
    ]
