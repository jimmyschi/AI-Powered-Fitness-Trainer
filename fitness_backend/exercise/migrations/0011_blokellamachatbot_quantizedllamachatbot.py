# Generated by Django 5.1.5 on 2025-03-17 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0010_deepseekchatbot'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlokeLlamaChatbot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='QuantizedLlamaChatbot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
