# Generated by Django 4.1.7 on 2023-03-30 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Rapid7ToneDetermination", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user", name="userName", field=models.CharField(max_length=128),
        ),
    ]