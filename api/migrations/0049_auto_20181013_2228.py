# Generated by Django 2.0.4 on 2018-10-13 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_auto_20181013_2117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='school_year',
            new_name='school_year_id'),
        migrations.RenameField(
            model_name='user',
            old_name='department',
            new_name='department_id'),
    ]
