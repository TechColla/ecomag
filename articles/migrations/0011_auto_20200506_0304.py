# Generated by Django 2.2.7 on 2020-05-06 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20200220_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'get_latest_by': ['-date'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Title'),
        ),
    ]