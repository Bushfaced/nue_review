# Generated by Django 4.0.4 on 2022-05-16 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_amenity_alter_venue_options_venue_amenities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity',
            name='category',
            field=models.CharField(choices=[('Health', 'Health'), ('Food', 'Food'), ('Drinks', 'Drinks'), ('Misc', 'Misc')], max_length=19),
        ),
    ]