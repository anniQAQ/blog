# Generated by Django 2.1.8 on 2020-06-21 03:49

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_articlepost_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(upload_to='article/%Y%m%d'),
        ),
    ]
