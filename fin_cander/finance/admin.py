from django.contrib import admin
from .models import PeriodTime, Income, Plan, Expense

# Register your models here.
admin.site.register(PeriodTime)
admin.site.register(Income)
admin.site.register(Plan)
admin.site.register(Expense)
