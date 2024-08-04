# Generated by Django 5.0.7 on 2024-08-03 11:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("memorialHall", "0002_alter_memorialhall_info_alter_wreath_comment"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="memorialhall",
            name="creator",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_halls",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
