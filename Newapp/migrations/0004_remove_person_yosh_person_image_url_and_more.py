# Generated by Django 5.0.4 on 2024-05-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0003_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='yosh',
        ),
        migrations.AddField(
            model_name='person',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='familya',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='ism',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='lavozim',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='tel',
            field=models.CharField(max_length=20),
        ),
    ]
