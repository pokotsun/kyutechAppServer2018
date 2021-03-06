# Generated by Django 2.0.4 on 2019-05-05 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0063_auto_20190310_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllabus',
            name='open_year',
            field=models.IntegerField(default=2018),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userschedule',
            name='syllabus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Syllabus'),
        ),
    ]
