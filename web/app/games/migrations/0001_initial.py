# Generated by Django 4.0.4 on 2022-06-06 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('championships', '0004_alter_championship_golden_ball_and_more'),
        ('stadiums', '0001_initial'),
        ('countries', '0008_alter_hostcountry_championship_and_more'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_country_home', models.IntegerField(verbose_name='Goals Country Home')),
                ('goals_country_guest', models.IntegerField(verbose_name='Goals Country Guest')),
                ('tickets', models.IntegerField(verbose_name='Tickets')),
                ('audience', models.IntegerField(verbose_name='Audience')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('win_condition', models.CharField(blank=True, max_length=255, null=True, verbose_name='Winner Condition')),
                ('championship', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='championships.championship', verbose_name='Championship')),
                ('country_guest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_country_guest', to='countries.country', verbose_name='Country Guest')),
                ('country_home', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_country_home', to='countries.country', verbose_name='Country Home')),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='games.phase', verbose_name='Phase')),
                ('stadium', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stadiums.stadium', verbose_name='Stadium')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=10, null=True, verbose_name='Color')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='games.game', verbose_name='Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='players.player', verbose_name='Player')),
            ],
        ),
    ]