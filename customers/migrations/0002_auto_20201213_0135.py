# Generated by Django 3.1.3 on 2020-12-13 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='customer',
        ),
    ]
