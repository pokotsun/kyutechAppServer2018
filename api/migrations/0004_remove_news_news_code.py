# Generated by Django 2.0.4 on 2018-04-12 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180412_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_code',
        ),
    ]
