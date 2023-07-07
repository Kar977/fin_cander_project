from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import PeriodTime, Income, Plan, Expense


@receiver(pre_save, sender=Income)
def create_period_time(sender, instance, **kwargs):
	# print("DUPA1", sender., flush=True)
	# period_time = PeriodTime.objects.create(year=year, month=month) # TODO get_or_create
	# sender.date_period = period_time
	pass

# @receiver(pre_save, sender=Income)
# def save_period_time(sender, instance, **kwargs):
# 	instance.periodtime.save()

