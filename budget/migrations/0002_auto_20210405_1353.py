# Generated by Django 3.0.9 on 2021-04-05 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetentry',
            name='actual',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='budgetentry',
            name='projected',
            field=models.PositiveIntegerField(),
        ),
    ]
