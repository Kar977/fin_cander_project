from django.contrib import admin
from .models import PeriodTime, Income, Plan, Expense

admin.site.register([PeriodTime, Income, Plan, Expense])
