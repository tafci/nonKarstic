# Generated by Django 2.0.3 on 2018-04-07 08:05

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cave',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]
