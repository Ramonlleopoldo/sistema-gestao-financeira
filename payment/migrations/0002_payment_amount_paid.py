# Generated by Django 5.1.5 on 2025-01-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount_paid',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
