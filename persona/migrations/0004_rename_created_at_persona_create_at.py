# Generated by Django 5.1.1 on 2024-10-13 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_rename_create_at_persona_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='created_at',
            new_name='create_at',
        ),
    ]
