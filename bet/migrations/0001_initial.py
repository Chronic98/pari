# Generated by Django 2.0.6 on 2018-06-14 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchKoef',
            fields=[
                ('match_id', models.IntegerField(primary_key=True, serialize=False)),
                ('bet_team_id', models.IntegerField()),
                ('perc', models.IntegerField()),
                ('koef', models.FloatField()),
            ],
            options={
                'db_table': 'match_koef',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('bet_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='KindOfSport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('kind_sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bet.KindOfSport')),
            ],
        ),
        migrations.CreateModel(
            name='LeagueMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bet.League')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('card', models.CharField(max_length=20)),
                ('operation_type', models.CharField(max_length=50)),
                ('transaction_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('account_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('full_name', models.CharField(max_length=250)),
                ('birthday', models.DateField()),
                ('country', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('balance', models.FloatField(default=0)),
                ('frozen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('kind_sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bet.KindOfSport')),
            ],
        ),
        migrations.CreateModel(
            name='Draw',
            fields=[
                ('match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bet.Match')),
            ],
        ),
        migrations.CreateModel(
            name='MatchMembers',
            fields=[
                ('match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bet.Match')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_id', to='bet.Teams')),
                ('title_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title_id', to='bet.Teams')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bet.Match')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bet.League')),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bet.Match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bet.Teams')),
            ],
        ),
        migrations.AddField(
            model_name='operation',
            name='account_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bet.Player'),
        ),
        migrations.AddField(
            model_name='leaguemembers',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bet.Teams'),
        ),
        migrations.AddField(
            model_name='bet',
            name='account_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bet.Player'),
        ),
        migrations.AddField(
            model_name='bet',
            name='bet_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bet.Teams'),
        ),
        migrations.AddField(
            model_name='bet',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bet.Match'),
        ),
    ]
