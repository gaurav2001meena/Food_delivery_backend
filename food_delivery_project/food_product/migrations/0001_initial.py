# Generated by Django 4.1.4 on 2022-12-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pipo', models.CharField(default='this is a pipo test', max_length=50, null=True)),
            ],
        ),
    ]