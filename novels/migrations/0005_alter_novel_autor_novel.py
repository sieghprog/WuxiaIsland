# Generated by Django 4.0.4 on 2022-05-07 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('novels', '0004_novel_categoria_novel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel',
            name='autor_novel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]