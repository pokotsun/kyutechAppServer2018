# Generated by Django 2.0.4 on 2018-04-25 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20180424_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='syllabus',
            old_name='target_hour',
            new_name='target_period',
        ),
    ]
