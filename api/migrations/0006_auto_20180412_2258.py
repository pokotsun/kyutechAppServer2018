# Generated by Django 2.0.4 on 2018-04-12 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180412_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='current_url',
            new_name='url',
        ),
    ]
