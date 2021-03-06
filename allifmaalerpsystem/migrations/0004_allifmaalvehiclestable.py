# Generated by Django 3.2.4 on 2021-07-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allifmaalerpsystem', '0003_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllifmaalVehiclesTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('vehicle_make', models.CharField(blank=True, max_length=255, null=True)),
                ('vehicle_model', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('license', models.CharField(blank=True, max_length=255, null=True)),
                ('vin', models.CharField(blank=True, max_length=255, null=True)),
                ('starting_odometer', models.IntegerField(blank=True, default='0', null=True)),
                ('primary_meter', models.CharField(blank=True, choices=[('Kilometers', 'Kilometers'), ('Miles', 'Miles')], max_length=255, null=True)),
                ('vehicle_type', models.CharField(blank=True, choices=[('Truck', 'Truck'), ('Car', 'Car'), ('Pickup', 'Pickup'), ('Bus', 'Bus'), ('Trailer', 'Trailer'), ('Van', 'Van'), ('Tow Truck', 'Tow Truck'), ('Motorcycle', 'Motorcycle')], max_length=255, null=True)),
                ('vehicle_status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=255, null=True)),
            ],
        ),
    ]
