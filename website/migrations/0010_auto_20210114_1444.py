# Generated by Django 3.1.4 on 2021-01-14 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20210113_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=30)),
                ('barva', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('kategorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='website.category')),
                ('splneno', models.ManyToManyField(to='website.UserProfile')),
            ],
        ),
        migrations.RemoveField(
            model_name='challenge_sc',
            name='splneno',
        ),
        migrations.RemoveField(
            model_name='challenge_zn',
            name='splneno',
        ),
        migrations.DeleteModel(
            name='Challenge_PR',
        ),
        migrations.DeleteModel(
            name='Challenge_SC',
        ),
        migrations.DeleteModel(
            name='Challenge_ZN',
        ),
    ]
