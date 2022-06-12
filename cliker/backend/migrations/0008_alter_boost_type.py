# Generated by Django 3.2 on 2022-06-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_boost_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'auto'), (0, 'casual')], default=0),
        ),
    ]
