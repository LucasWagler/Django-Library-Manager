# Generated by Django 3.1.3 on 2020-11-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManager', '0005_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='address_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='address_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='postal_code',
            field=models.IntegerField(blank=True, default=44444, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='state',
            field=models.CharField(blank=True, default='NY', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(default=12.99),
        ),
    ]