# Generated by Django 4.2.7 on 2023-11-26 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GPSData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('velocity', models.FloatField()),
                ('satellites', models.IntegerField()),
                ('bearing', models.CharField(max_length=20)),
            ],
        ),
    ]
