# Generated by Django 2.2.1 on 2022-07-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
