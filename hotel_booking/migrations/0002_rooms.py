# Generated by Django 3.0.7 on 2020-08-05 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(choices=[('1', 'Premium'), ('2', 'Deluxe'), ('3', 'Basic')], max_length=50)),
                ('capacity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('size', models.IntegerField()),
                ('status', models.CharField(choices=[('1', 'Available'), ('2', 'not Available')], max_length=15)),
                ('roomnumber', models.IntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotels')),
            ],
        ),
    ]
