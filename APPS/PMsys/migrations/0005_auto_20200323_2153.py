# Generated by Django 2.2.6 on 2020-03-23 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PMsys', '0004_auto_20200317_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsfiles',
            name='path',
        ),
        migrations.AddField(
            model_name='itemsfiles',
            name='file',
            field=models.FileField(default=1, upload_to='media/procedure', verbose_name='文件位置'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemsfiles',
            name='memo',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='itemsfiles',
            name='title',
            field=models.CharField(default=1, max_length=32, verbose_name='文件名字'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemsfiles',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='填写人'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemsfiles',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(1, '入场手续'), (2, '验收单'), (3, '质量检验单'), (4, '其它')], null=True, verbose_name='文件类型'),
        ),
        migrations.AlterField(
            model_name='windpower',
            name='tier',
            field=models.FloatField(blank=True, null=True, verbose_name='塔筒层数'),
        ),
    ]
