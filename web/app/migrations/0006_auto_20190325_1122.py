# Generated by Django 2.1.7 on 2019-03-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rubro_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='subproducto',
            name='image2',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='subproducto',
            name='image3',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='subproducto',
            name='image',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]