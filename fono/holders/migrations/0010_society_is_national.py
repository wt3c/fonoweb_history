# Generated by Django 4.1.1 on 2022-09-20 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("holders", "0009_auto_20211223_1946"),
    ]

    operations = [
        migrations.AddField(
            model_name="society",
            name="is_national",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
