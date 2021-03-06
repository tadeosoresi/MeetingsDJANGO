# Generated by Django 2.2.5 on 2021-01-26 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
                ('sex', models.CharField(max_length=1)),
                ('provincia', models.CharField(max_length=30)),
                ('codigo_postal', models.IntegerField()),
            ],
        ),
    ]
