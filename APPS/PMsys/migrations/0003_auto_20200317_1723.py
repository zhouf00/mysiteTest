# Generated by Django 2.2.6 on 2020-03-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMsys', '0002_auto_20200316_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsensors',
            name='number',
            field=models.CharField(default=1, max_length=32, verbose_name='通道编号'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemsensors',
            name='s_title',
            field=models.CharField(max_length=128, null=True, unique=True, verbose_name='传感器编号'),
        ),
    ]