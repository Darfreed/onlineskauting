# Generated by Django 3.1.4 on 2021-01-13 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20210113_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge_pr',
            name='splneno',
            field=models.ManyToManyField(to='website.UserProfile'),
        ),
        migrations.AlterField(
            model_name='challenge_sc',
            name='splneno',
            field=models.ManyToManyField(to='website.UserProfile'),
        ),
        migrations.AlterField(
            model_name='challenge_zn',
            name='splneno',
            field=models.ManyToManyField(to='website.UserProfile'),
        ),
    ]
