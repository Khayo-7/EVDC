# Generated by Django 3.1.3 on 2020-11-28 06:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20201127_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assign_vehicle',
            name='assign_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 570007), verbose_name='date assigned'),
        ),
        migrations.AlterField(
            model_name='assign_vehicle',
            name='length',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 569043), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 564020), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 567049), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='machine_data',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 567049), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 564020), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='route',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 568046), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='routetypes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 568046)),
        ),
        migrations.AlterField(
            model_name='station',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 566054), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='subcity',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 565056), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 565056), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='vehicles_location',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 570007), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='waiting_time',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 22, 44, 46, 569043), verbose_name='date registerd'),
        ),
    ]
