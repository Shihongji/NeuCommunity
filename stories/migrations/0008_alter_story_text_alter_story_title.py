# Generated by Django 4.1.7 on 2023-03-22 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_alter_story_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
