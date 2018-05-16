# Generated by Django 2.0.4 on 2018-05-16 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20180516_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='academic_credit_infos',
            field=models.CharField(max_length=750),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='keywords',
            field=models.CharField(max_length=750, null=True),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='notes',
            field=models.CharField(max_length=750, null=True),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='study_aid_books',
            field=models.CharField(max_length=750, null=True),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='teacher_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='text_books',
            field=models.CharField(max_length=750, null=True),
        ),
        migrations.AlterField(
            model_name='userschedule',
            name='syllabus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Syllabus'),
        ),
    ]