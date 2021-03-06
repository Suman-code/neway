# Generated by Django 3.1.4 on 2021-08-06 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andra Pradesh', 'Andra Pradesh'), ('Arunalchal Pradesh', 'Arunacahl Pradesh'), ('Andaman', 'Andaman'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Karnataka', 'KArnataka'), ('Tamil Nadu', 'Tamil Nadu'), ('Kerala', 'Kerala'), ('Telengana', 'Telengana'), ('Jharkhand', 'Jharkhand'), ('Gujraj', 'Gujrrat'), ('Maharastra', 'Maharastara'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Nagaland', 'Nagaland'), ('Mizoram', 'Mizoram'), ('Punjab', 'Punjab'), ('J&K', 'J&K'), ('Himachal Pradesh', 'Hiamchal Pradesh'), ('Goa', 'Goa'), ('Tripura', 'Tripura'), ('Hariyana', 'Hariyana')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titile', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('M', 'Mobile'), ('TW', 'Top wear'), ('WB', 'Bottom wear'), ('L', 'Laptop'), ('TND', 'Trending')], max_length=3)),
                ('product_image', models.ImageField(upload_to='producting')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_Date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Andra Pradesh', 'Andra Pradesh'), ('Arunalchal Pradesh', 'Arunacahl Pradesh'), ('Andaman', 'Andaman'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Karnataka', 'KArnataka'), ('Tamil Nadu', 'Tamil Nadu'), ('Kerala', 'Kerala'), ('Telengana', 'Telengana'), ('Jharkhand', 'Jharkhand'), ('Gujraj', 'Gujrrat'), ('Maharastra', 'Maharastara'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Nagaland', 'Nagaland'), ('Mizoram', 'Mizoram'), ('Punjab', 'Punjab'), ('J&K', 'J&K'), ('Himachal Pradesh', 'Hiamchal Pradesh'), ('Goa', 'Goa'), ('Tripura', 'Tripura'), ('Hariyana', 'Hariyana')], default='pending', max_length=50)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
