# Generated by Django 2.0.4 on 2018-10-13 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0057_auto_20181014_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userschedule',
            name='syllabus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Syllabus'),
        ),
    ]