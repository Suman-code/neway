# Generated by Django 3.1.4 on 2021-08-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210806_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('TW', 'Topwear'), ('WB', 'Bottomwear'), ('L', 'Laptop'), ('TND', 'Trending'), ('DOD', 'deal of the day')], max_length=3),
        ),
    ]
