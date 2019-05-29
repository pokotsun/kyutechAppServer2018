# Generated by Django 2.0.4 on 2019-05-15 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0066_auto_20190515_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('which_os', models.CharField(max_length=10)),
                ('evaluation', models.CharField(max_length=500)),
                ('opinion', models.CharField(max_length=512)),
                ('p_and_d_opinion', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'UserImpression',
            },
        ),
        migrations.AlterField(
            model_name='userschedule',
            name='syllabus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Syllabus'),
        ),
    ]