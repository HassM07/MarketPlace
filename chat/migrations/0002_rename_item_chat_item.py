# Generated by Django 4.2.2 on 2023-06-23 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='Item',
            new_name='item',
        ),
    ]