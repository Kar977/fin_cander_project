# Generated by Django 4.2.2 on 2023-07-11 16:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "finance",
            "0002_alter_expense_date_expense_alter_expense_date_period_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="date_expense",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 7, 11, 16, 6, 13, 853639, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="expense",
            name="date_period",
            field=models.ForeignKey(
                default=datetime.datetime(
                    2023, 7, 11, 16, 6, 13, 853639, tzinfo=datetime.timezone.utc
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
                    2023, 7, 11, 16, 6, 13, 852642, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="date_period",
            field=models.ForeignKey(
                default=datetime.datetime(
                    2023, 7, 11, 16, 6, 13, 853639, tzinfo=datetime.timezone.utc
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
                    2023, 7, 11, 16, 6, 13, 853639, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
