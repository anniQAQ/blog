# Generated by Django 2.2 on 2020-06-23 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_articlepost_stmp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepost',
            name='stmp',
        ),
        migrations.AddField(
            model_name='articlepost',
            name='idmax',
            field=models.PositiveIntegerField(default=0),
        ),
    ]