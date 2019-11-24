# Generated by Django 2.2.7 on 2019-11-24 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_auto_20191124_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team_A',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_A', to='teams.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_B',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_B', to='teams.Team'),
        ),
    ]