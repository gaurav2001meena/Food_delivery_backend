# Generated by Django 4.1.4 on 2022-12-26 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_product', '0002_food'),
        ('customers', '0003_order_email_alter_customers_email_alter_order_fid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.address')),
                ('fid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food_product.food')),
            ],
        ),
    ]
