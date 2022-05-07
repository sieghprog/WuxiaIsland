# Generated by Django 4.0.4 on 2022-05-07 18:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('novels', '0002_novel_status_novel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capitulo_numero', models.IntegerField(blank=True, null=True, verbose_name='Número')),
                ('capitulo_titulo', models.CharField(max_length=90, verbose_name='Título')),
                ('capitulo_texto', models.TextField()),
                ('capitulo_data', models.DateTimeField(default=django.utils.timezone.now)),
                ('capitulo_publicado', models.BooleanField(default=False, verbose_name='Publicado')),
                ('capitulo_novel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='novels.novel')),
            ],
        ),
    ]
