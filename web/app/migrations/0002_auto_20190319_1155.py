# Generated by Django 2.1.7 on 2019-03-19 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subproducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=40)),
                ('stock', models.IntegerField(null=True)),
                ('precio', models.FloatField(null=True)),
                ('image', models.CharField(max_length=1024)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='image',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='tipo',
        ),
        migrations.AddField(
            model_name='subproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Producto'),
        ),
    ]