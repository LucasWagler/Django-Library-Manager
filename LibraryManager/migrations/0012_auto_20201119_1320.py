# Generated by Django 3.1.3 on 2020-11-19 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManager', '0011_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='../book_img'),
        ),
    ]