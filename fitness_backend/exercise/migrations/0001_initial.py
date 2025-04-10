# Generated by Django 5.1.5 on 2025-01-23 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_upload', models.FileField(upload_to='uploads/')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('exercise_weight', models.IntegerField(blank=True, null=True)),
                ('forces', models.JSONField(blank=True, null=True)),
                ('angles', models.JSONField(blank=True, null=True)),
                ('concentric_times', models.JSONField(blank=True, null=True)),
                ('eccentric_times', models.JSONField(blank=True, null=True)),
                ('reps', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('body_weight', models.IntegerField()),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
            ],
        ),
    ]
