# Generated by Django 2.0.4 on 2018-05-16 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20180516_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userschedule',
            name='syllabus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Syllabus'),
        ),
    ]
