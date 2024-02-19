# Generated by Django 4.2.7 on 2024-01-02 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('CarPlate', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('CarType', models.TextField(max_length=30)),
                ('Capacity', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('ClientID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Clientname', models.TextField(max_length=50)),
                ('Clientphone', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Rental_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TotalPaid', models.PositiveIntegerField(blank=True, null=True)),
                ('Startdate', models.DateTimeField(blank=True, null=True)),
                ('returndate', models.DateTimeField(blank=True, null=True)),
                ('CarPlate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
                ('ClientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.client')),
            ],
        ),
    ]