# Generated by Django 4.0.1 on 2022-02-03 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0021_alter_rentalbooking_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalbooking',
            name='rental_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rentalbooking',
            name='return_date',
            field=models.DateField(),
        ),
    ]