# Generated by Django 4.0.4 on 2022-05-07 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_alter_categoria_categoria'),
        ('novels', '0003_remove_novel_categoria_novel'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='categoria_novel',
            field=models.ManyToManyField(to='categorias.categoria', verbose_name='Categoria'),
        ),
    ]