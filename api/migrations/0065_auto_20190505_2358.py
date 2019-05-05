# Generated by Django 2.0.4 on 2019-05-05 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0064_auto_20190505_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='open_year',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='target_period',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userschedule',
            name='syllabus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Syllabus'),
        ),
    ]