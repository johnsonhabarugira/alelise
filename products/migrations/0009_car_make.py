# Generated by Django 4.2 on 2023-05-14 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_part_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='make',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_makes', to='products.make'),
        ),
    ]
