# Generated by Django 2.0.4 on 2018-04-11 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_code', models.IntegerField()),
                ('infos', models.CharField(max_length=10000)),
                ('attachement_titles', models.CharField(max_length=10000)),
                ('attachement_urls', models.CharField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsHeading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color_code', models.CharField(max_length=20)),
                ('news_heading_code', models.IntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='news_heading',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.NewsHeading'),
        ),
    ]
