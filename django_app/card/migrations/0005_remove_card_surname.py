# Generated by Django 4.2.6 on 2024-04-30 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_remove_card_name_card_first_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='surname',
        ),
    ]
