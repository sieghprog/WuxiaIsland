# Generated by Django 4.0.4 on 2022-05-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='status_novel',
            field=models.CharField(choices=[('Complete', 'Complete'), ('Ongoing', 'Ongoing')], default='Ongoing', max_length=8),
        ),
    ]