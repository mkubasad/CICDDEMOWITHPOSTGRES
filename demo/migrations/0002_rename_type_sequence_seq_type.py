# Generated by Django 5.1.4 on 2024-12-24 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sequence',
            old_name='Type',
            new_name='seq_type',
        ),
    ]
