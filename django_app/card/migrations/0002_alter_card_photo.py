# Generated by Django 4.2.6 on 2024-04-30 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='photo',
            field=models.FileField(null=True, upload_to='photo'),
        ),
    ]
