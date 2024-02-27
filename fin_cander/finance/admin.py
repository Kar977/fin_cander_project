from django.contrib import admin

from users.models import Profile
from finance.models import PeriodTime, Income, Plan, Expense

admin.site.register([PeriodTime, Income, Plan, Expense, Profile])
