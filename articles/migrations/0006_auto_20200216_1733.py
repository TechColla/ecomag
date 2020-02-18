# Generated by Django 2.2.7 on 2020-02-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200209_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Nom de produit'),
        ),
    ]
