# Generated by Django 3.1.3 on 2020-11-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManager', '0004_auto_20201119_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=12.0),
        ),
    ]
