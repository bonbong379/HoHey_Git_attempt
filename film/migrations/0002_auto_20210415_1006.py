# Generated by Django 3.1 on 2021-04-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film_profile',
            name='film_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]