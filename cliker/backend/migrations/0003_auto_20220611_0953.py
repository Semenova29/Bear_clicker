# Generated by Django 3.2 on 2022-06-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20220611_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='core',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
