# Generated by Django 2.2.2 on 2019-06-17 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marcas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
