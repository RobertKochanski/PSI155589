# Generated by Django 3.2.9 on 2022-01-07 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=45)),
                ('lastName', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=45)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('comments', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnimalHotel.animal')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnimalHotel.species'),
        ),
        migrations.AddField(
            model_name='animal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnimalHotel.user'),
        ),
    ]
