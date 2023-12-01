# Generated by Django 4.2.7 on 2023-11-22 20:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jewelry',
            name='ID',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1, message='ID should be a positive integer.')]),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='code',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\w{5}/\\w-\\w{2}$', message='Error. The code should be in the correct format.')]),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='date_of_creation',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator('2023-11-22', message="The date can't be in the future.")]),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='jewelry_type',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^(rings|earrings|bracelets)$', message='Invalid type of jewelry.')]),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='material',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^(gold|silver|platinum)$', message='Invalid material option.')]),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.RegexValidator('^\\d+\\.\\d[1-9]?$', message='Please enter a valid price.')]),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='title',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]+$', message='The name should only contain letters of the alphabet.')]),
        ),
    ]
