# Generated by Django 4.2.6 on 2024-04-30 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_alter_card_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='name',
        ),
        migrations.AddField(
            model_name='card',
            name='first_last_name',
            field=models.CharField(default='undefined', max_length=255),
            preserve_default=False,
        ),
    ]
