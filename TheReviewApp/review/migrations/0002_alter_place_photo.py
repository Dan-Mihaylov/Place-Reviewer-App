# Generated by Django 5.0.1 on 2024-01-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='photo',
            field=models.URLField(default='https://www.invoicera.com/wp-content/uploads/2023/11/default-image.jpg'),
        ),
    ]
