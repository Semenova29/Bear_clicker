# Generated by Django 3.2 on 2022-06-10 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='core',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Boost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=10)),
                ('power', models.IntegerField(default=1)),
                ('core', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.core')),
            ],
        ),
    ]
