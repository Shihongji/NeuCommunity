# Generated by Django 4.1.7 on 2023-03-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0009_remove_comment_upvotes_remove_story_upvotes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='story',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
