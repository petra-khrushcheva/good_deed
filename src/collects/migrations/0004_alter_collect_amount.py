# Generated by Django 5.0.6 on 2024-06-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("collects", "0003_alter_collect_amount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collect",
            name="amount",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=9,
                null=True,
                verbose_name="Запланированная сумма",
            ),
        ),
    ]
