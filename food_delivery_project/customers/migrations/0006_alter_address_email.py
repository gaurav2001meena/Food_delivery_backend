# Generated by Django 4.1.4 on 2022-12-26 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_address_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customers'),
        ),
    ]