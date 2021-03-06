# Generated by Django 2.2.7 on 2020-02-09 20:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
        ('articles', '0004_auto_20200204_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.IntegerField(verbose_name='rating')),
                ('content', models.TextField(max_length=200, verbose_name='Comment')),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Product')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.UserProfileInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1, verbose_name='amount')),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Product')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.UserProfileInfo')),
            ],
        ),
    ]
