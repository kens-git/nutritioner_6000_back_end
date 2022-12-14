# Generated by Django 4.0.6 on 2022-08-22 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_alter_consumablecategory_name_alter_nutrient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyvalue',
            name='nutrient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.nutrient'),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api.name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='consumable',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='unit', to='api.unit'),
        ),
        migrations.AlterField(
            model_name='nutrient',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nutrient_unit', to='api.unit'),
        ),
    ]
