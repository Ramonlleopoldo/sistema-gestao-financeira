# Generated by Django 5.1.5 on 2025-02-04 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_expense_installment_count_installment'),
    ]

    operations = [
        migrations.AddField(
            model_name='installment',
            name='status',
            field=models.CharField(choices=[('Pago', 'Pago'), ('Em dia', 'Em dia'), ('Atrasado', 'Atrasado')], default=0, max_length=40),
            preserve_default=False,
        ),
    ]
