# Generated by Django 4.0.1 on 2022-01-31 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0003_delete_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=15)),
                ('inventory', models.IntegerField()),
            ],
        ),
    ]
