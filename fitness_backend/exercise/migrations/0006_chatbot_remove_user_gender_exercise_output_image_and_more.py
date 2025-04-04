# Generated by Django 5.1.5 on 2025-02-08 17:15

import storages.backends.gcloud
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_user_is_active_user_is_staff_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatbot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.AddField(
            model_name='exercise',
            name='output_image',
            field=models.FileField(blank=True, null=True, storage=storages.backends.gcloud.GoogleCloudStorage, upload_to='progress_images/'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='body_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
