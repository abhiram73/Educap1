# Generated by Django 3.1.2 on 2020-11-03 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_wishlistitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]