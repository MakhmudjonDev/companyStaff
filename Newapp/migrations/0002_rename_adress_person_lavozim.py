# Generated by Django 5.0.4 on 2024-05-13 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='adress',
            new_name='lavozim',
        ),
    ]
