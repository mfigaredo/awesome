# Generated by Django 4.2 on 2024-04-03 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_landingpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='access_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
