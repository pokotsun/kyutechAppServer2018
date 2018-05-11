# Generated by Django 2.0.4 on 2018-05-09 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20180430_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='userschedule',
            name='memo',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='userschedule',
            name='syllabus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Syllabus'),
        ),
    ]
