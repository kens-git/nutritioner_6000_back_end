# Generated by Django 4.0.4 on 2022-09-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_name_plural'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrient',
            name='is_macronutrient',
            field=models.BooleanField(default=False),
        ),
    ]
