# Generated by Django 4.2.2 on 2024-01-05 16:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "finance",
            "0011_alter_expense_date_expense_alter_expense_date_period_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="date_expense",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 1, 5, 16, 41, 14, 890264, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="expense",
            name="date_period",
            field=models.ForeignKey(
                default=datetime.datetime(
                    2024, 1, 5, 16, 41, 14, 890208, tzinfo=datetime.timezone.utc
                ),
                on_delete=django.db.models.deletion.CASCADE,
                to="finance.periodtime",
            ),
        ),
        migrations.AlterField(
            model_name="income",
            name="date_income",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 1, 5, 16, 41, 14, 889004, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="date_period",
            field=models.ForeignKey(
                default=datetime.datetime(
                    2024, 1, 5, 16, 41, 14, 889499, tzinfo=datetime.timezone.utc
                ),
                on_delete=django.db.models.deletion.CASCADE,
                to="finance.periodtime",
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="date_plan",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 1, 5, 16, 41, 14, 889688, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
