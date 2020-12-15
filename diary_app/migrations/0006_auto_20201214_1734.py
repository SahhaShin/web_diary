# Generated by Django 3.1.2 on 2020-12-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary_app', '0005_auto_20201214_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='year1',
        ),
        migrations.AddField(
            model_name='diary',
            name='month1',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='monthly',
            name='month2',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='yearly',
            name='year1',
            field=models.IntegerField(default=2021),
        ),
    ]
