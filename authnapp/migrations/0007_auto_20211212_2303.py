# Generated by Django 2.2.25 on 2021-12-12 23:03

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0006_auto_20211208_1823"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 12, 14, 23, 3, 36, 478931, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        ),
    ]
