# Generated by Django 3.1.3 on 2020-11-06 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201105_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedarticles',
            name='article_id',
        ),
        migrations.RemoveField(
            model_name='savedarticles',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='SavedArticles',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
