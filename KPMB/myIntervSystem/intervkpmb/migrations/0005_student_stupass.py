# Generated by Django 5.0.2 on 2024-02-23 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intervkpmb', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stuPass',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]