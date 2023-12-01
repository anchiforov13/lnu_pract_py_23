# Generated by Django 4.2.7 on 2023-11-22 20:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry_app', '0003_remove_jewelry_id_jewelry_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jewelry',
            name='ID',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1, message='ID should be a positive integer.')]),
        ),
    ]
