# Generated by Django 3.1.3 on 2023-02-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
