# Generated by Django 3.0.2 on 2020-01-26 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Catégorie', 'verbose_name_plural': 'Catégories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='mainimage',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='articles.Category'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=300)),
        ),
        migrations.AddField(
            model_name='product',
            name='mainImage',
            field=models.ImageField(blank=True, upload_to='products/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='detail_text',
            field=models.TextField(max_length=1000, verbose_name='Desciption du produit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Nom de produit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='preview_text',
            field=models.TextField(max_length=200, verbose_name='Description courte'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('slug', 'parent')},
        ),
    ]