# Generated by Django 3.1.3 on 2020-11-19 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManager', '0010_auto_20201119_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./book_img'),
        ),
    ]