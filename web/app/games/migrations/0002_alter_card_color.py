# Generated by Django 4.0.4 on 2022-06-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(blank=True, choices=[('yellow', 'YELLOW'), ('red', 'RED')], max_length=6, null=True, verbose_name='Color'),
        ),
    ]
