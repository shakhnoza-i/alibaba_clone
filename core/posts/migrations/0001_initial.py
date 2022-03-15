# Generated by Django 3.2.12 on 2022-03-14 16:35

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('currency', models.CharField(choices=[('KZT', 'KZT'), ('USD', 'USD'), ('EUR', 'EUR'), ('RUB', 'RUB'), ('CNY', 'CNY')], default='KZT', max_length=10)),
                ('min_order', models.PositiveIntegerField(default=1)),
                ('measure', models.CharField(max_length=20)),
                ('category', models.PositiveSmallIntegerField(choices=[(0, 'Agriculture & Food'), (1, 'Apparel,Textiles & Accessories'), (2, 'Auto & Transportation'), (3, 'Bags, Shoes & Accessories'), (4, 'Electronics'), (5, 'Electrical Equipment, Components & Telecoms'), (6, 'Gifts, Sports & Toys'), (7, 'Health & Beauty'), (8, 'Home, Lights & Construction'), (9, 'Machinery, Industrial Parts & Tools'), (10, 'Metallurgy, Chemicals, Rubber & Plastics'), (11, 'Packaging, Advertising & Office')], default=0)),
                ('availability', models.PositiveSmallIntegerField(choices=[(0, 'In stock'), (1, 'Will be available soon. Check with the manager'), (2, 'On order'), (3, 'Availability unknown')], default=0)),
                ('detailed_description', models.CharField(max_length=3000, null=True)),
                ('image', models.ImageField(null=True, upload_to=posts.models.post_image_file_path)),
            ],
        ),
    ]
