# Generated by Django 4.2.6 on 2023-10-26 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=45)),
                ('marca', models.CharField(max_length=45)),
                ('modelo', models.CharField(max_length=45)),
            ],
        ),
    ]
