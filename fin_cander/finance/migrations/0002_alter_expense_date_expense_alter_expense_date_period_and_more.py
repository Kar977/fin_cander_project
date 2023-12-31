# Generated by Django 4.2.2 on 2023-07-10 17:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="date_expense",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 7, 10, 17, 54, 7, 927478, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="expense",
            name="date_period",
            field=models.ForeignKey(
                default=datetime.datetime(
                    2023, 7, 10, 17, 54, 7, 927478, tzinfo=datetime.timezone.utc
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
                    2023, 7, 10, 17, 54, 7, 926478, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="periodtime",
            name="month",
            field=models.IntegerField(default=7),
        ),
        migrations.AlterField(
            model_name="plan",
            name="date_period",
            field=models.ForeignKey(
                default=datetime.datetime(
                    2023, 7, 10, 17, 54, 7, 927478, tzinfo=datetime.timezone.utc
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
                    2023, 7, 10, 17, 54, 7, 927478, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
