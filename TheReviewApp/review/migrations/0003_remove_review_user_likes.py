# Generated by Django 5.0.1 on 2024-01-30 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_remove_review_user_likes_review_user_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user_likes',
        ),
    ]
