# Generated by Django 4.2.7 on 2024-02-19 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intervention', '0004_delete_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointmentDate', models.DateField()),
                ('venue', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('purpose', models.TextField(blank=True, null=True)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intervention.mentor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intervention.student')),
            ],
        ),
    ]