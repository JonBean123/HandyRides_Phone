# Generated by Django 5.0.2 on 2024-02-23 02:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rides", "0004_person_vehicle_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="phone_number",
            field=models.CharField(default=str, max_length=20),
            preserve_default=False,
        ),
    ]