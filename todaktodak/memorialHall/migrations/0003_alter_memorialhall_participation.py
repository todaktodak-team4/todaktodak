# Generated by Django 5.0.7 on 2024-07-24 10:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("memorialHall", "0002_memorialhall_token"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="memorialhall",
            name="participation",
            field=models.ManyToManyField(
                blank=True,
                related_name="participation_halls",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]