# Generated by Django 2.0.4 on 2018-10-12 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20181012_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userschedule',
            name='syllabus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Syllabus'),
        ),
    ]
