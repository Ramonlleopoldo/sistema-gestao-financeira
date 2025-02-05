# Generated by Django 5.1.5 on 2025-01-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_student_status_payment_alter_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Parou', 'Parou'), ('Novo', 'Novo'), ('Retornou', 'Retornou')], max_length=50, null=True),
        ),
    ]
