# Generated by Django 2.2 on 2020-06-22 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20200623_0402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepost',
            name='next',
        ),
        migrations.RemoveField(
            model_name='articlepost',
            name='previous',
        ),
    ]
