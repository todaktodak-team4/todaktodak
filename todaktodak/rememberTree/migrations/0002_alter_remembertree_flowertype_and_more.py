# Generated by Django 5.0.7 on 2024-07-19 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rememberTree', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remembertree',
            name='flowerType',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='remembertree',
            name='myName',
            field=models.CharField(default='토닥토닥', max_length=100),
        ),
        migrations.AlterField(
            model_name='remembertree',
            name='treeName',
            field=models.CharField(max_length=20),
        ),
    ]
