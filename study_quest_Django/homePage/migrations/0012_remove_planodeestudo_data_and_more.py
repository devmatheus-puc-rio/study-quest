# Generated by Django 5.1.2 on 2024-12-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0011_alter_planodeestudo_visibilidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planodeestudo',
            name='data',
        ),
        migrations.AlterField(
            model_name='planodeestudo',
            name='avaliacao',
            field=models.FloatField(default=10),
        ),
        migrations.AlterField(
            model_name='planodeestudo',
            name='descricao',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='planodeestudo',
            name='identificacao',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='planodeestudo',
            name='titulo',
            field=models.CharField(default='', max_length=200),
        ),
    ]
