# Generated by Django 5.1.2 on 2024-11-27 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0003_alter_planodeestudo_identificacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planodeestudo',
            name='descricao',
            field=models.CharField(max_length=500),
        ),
    ]
