# Generated by Django 4.0.1 on 2022-02-03 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0018_alter_rentalbooking_rental_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentalbooking',
            old_name='CustomerName',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='rentalbooking',
            old_name='vehicle_type',
            new_name='vehicle',
        ),
    ]
