# Generated by Django 2.2 on 2020-06-22 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_articlepost_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='next',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='articlepost',
            name='previous',
            field=models.BooleanField(default=False),
        ),
    ]
