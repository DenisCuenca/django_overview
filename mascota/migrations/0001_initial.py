# Generated by Django 4.1.5 on 2023-01-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('raza', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('altura', models.FloatField()),
                ('estaVacunado', models.BooleanField(default=False)),
            ],
        ),
    ]
