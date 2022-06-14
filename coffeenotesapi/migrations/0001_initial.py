# Generated by Django 4.0.4 on 2022-06-13 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrewingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='FlavorNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=55)),
                ('password', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('image', models.ImageField(upload_to='images')),
                ('grind_setting', models.CharField(max_length=10)),
                ('rating', models.CharField(max_length=5)),
                ('notes', models.CharField(max_length=200)),
                ('brewing_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeenotesapi.brewingmethod')),
                ('flavor_profile', models.ManyToManyField(to='coffeenotesapi.flavornote')),
            ],
        ),
    ]
