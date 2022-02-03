# Generated by Django 4.0.1 on 2022-02-01 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0004_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField()),
                ('return_date', models.DateField(default=0)),
                ('CustomerName', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='rentalapp.customer')),
                ('vehicle_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='rentalapp.vehicle')),
            ],
        ),
    ]
