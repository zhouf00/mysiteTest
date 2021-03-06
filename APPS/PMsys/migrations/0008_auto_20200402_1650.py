# Generated by Django 2.2.6 on 2020-04-02 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PMsys', '0007_auto_20200323_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemstay',
            name='memo',
            field=models.TextField(default=None, verbose_name='备注说明'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemstay',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='填写人'),
            preserve_default=False,
        ),
    ]
