# Generated by Django 4.0.4 on 2022-05-11 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('tshirt_name', models.CharField(max_length=255, verbose_name='T-shirt Name')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='countries.country', verbose_name='Country')),
            ],
        ),
    ]