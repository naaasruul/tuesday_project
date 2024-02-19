# Generated by Django 4.2.7 on 2024-02-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stuId', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.BooleanField(default=True)),
            ],
        ),
    ]
