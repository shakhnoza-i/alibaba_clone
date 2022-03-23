# Generated by Django 3.2.12 on 2022-03-23 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220321_0813'),
        ('review', '0002_auto_20220323_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='posts.post'),
        ),
    ]
