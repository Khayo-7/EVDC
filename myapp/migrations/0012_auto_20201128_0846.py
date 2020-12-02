# Generated by Django 3.1.3 on 2020-11-28 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20201128_0640'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='penalty',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='assign_vehicle',
            name='assign_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 696065), verbose_name='date assigned'),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 694071), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 690051), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 692079), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='machine_data',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 693073), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 691079), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 689088), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='route',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 693073), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='routetypes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 694071)),
        ),
        migrations.AlterField(
            model_name='station',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 692079), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='subcity',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 690051), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 691079), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='vehicles_location',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 695069), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='waiting_time',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 8, 46, 3, 695069), verbose_name='date registerd'),
        ),
    ]