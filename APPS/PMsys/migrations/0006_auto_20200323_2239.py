# Generated by Django 2.2.6 on 2020-03-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMsys', '0005_auto_20200323_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsfiles',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='文件位置'),
        ),
    ]