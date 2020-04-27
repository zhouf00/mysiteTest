# Generated by Django 2.2.6 on 2020-04-23 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PMsys', '0013_auto_20200421_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemexecutr',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='施工人员'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PersonTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=32, verbose_name='人员名字')),
                ('status', models.SmallIntegerField(verbose_name='施工人员状态')),
                ('begintime', models.DateTimeField(verbose_name='开始时间')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMsys.Items')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]