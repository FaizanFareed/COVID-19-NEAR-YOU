# Generated by Django 3.0.7 on 2020-07-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19nearyou', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmedcaselocation',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]