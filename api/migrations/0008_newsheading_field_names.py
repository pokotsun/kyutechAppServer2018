# Generated by Django 2.0.4 on 2018-04-13 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180412_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsheading',
            name='field_names',
            field=models.CharField(default='aiue', max_length=1000),
            preserve_default=False,
        ),
    ]
