# Generated by Django 5.0.4 on 2024-04-26 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, max_length=2500, null=True),
        ),
    ]
