# Generated by Django 2.1 on 2018-11-21 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming', '0002_auto_20181121_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='developer',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='stream',
            name='popularity',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='stream',
            name='summary',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='stream',
            name='total_rating',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='stream',
            name='total_rating_count',
            field=models.CharField(default='', max_length=200),
        ),
    ]
