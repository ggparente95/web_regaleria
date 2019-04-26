# Generated by Django 2.1.7 on 2019-03-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('stock', models.IntegerField()),
                ('precio', models.FloatField()),
                ('image', models.CharField(max_length=1024)),
            ],
        ),
    ]