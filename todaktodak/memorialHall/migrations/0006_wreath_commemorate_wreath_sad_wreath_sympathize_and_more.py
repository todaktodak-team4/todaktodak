# Generated by Django 5.0.7 on 2024-07-29 03:54

import memorialHall.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("memorialHall", "0005_alter_memorialhall_thumbnail"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="wreath",
            name="commemorate",
            field=models.ManyToManyField(
                related_name="com_wreath", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="wreath",
            name="sad",
            field=models.ManyToManyField(
                related_name="sad_wreath", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="wreath",
            name="sympathize",
            field=models.ManyToManyField(
                related_name="sym_wreath", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="wreath",
            name="todak",
            field=models.ManyToManyField(
                related_name="todak_wreath", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="wreath",
            name="together",
            field=models.ManyToManyField(
                related_name="together_wreath", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="memorialhall",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=memorialHall.models.get_thumbnail_upload_path,
                verbose_name="대표사진",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="todak",
            field=models.ManyToManyField(
                related_name="todak_mse", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
