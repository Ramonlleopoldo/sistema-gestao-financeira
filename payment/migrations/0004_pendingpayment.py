# Generated by Django 5.1.5 on 2025-01-23 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_alter_payment_amount_paid'),
        ('student', '0003_alter_student_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_pending', to='student.student')),
            ],
        ),
    ]
