# Generated by Django 5.0.1 on 2024-01-14 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='helpful_count',
            field=models.IntegerField(default=0),
        ),
    ]
