# Generated by Django 3.2.12 on 2022-03-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
