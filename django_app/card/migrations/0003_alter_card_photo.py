# Generated by Django 4.2.6 on 2024-04-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_alter_card_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='photo'),
        ),
    ]
