from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import PeriodTime, Income, Plan, Expense


@receiver(pre_save, sender=Income)
@receiver(pre_save, sender=Plan)
@receiver(pre_save, sender=Expense)
def create_period_time(sender, instance, created, **kwargs):
	if not created:
		PeriodTime.objects.create(sender=instance)


@receiver(pre_save, sender=Income)
@receiver(pre_save, signal=Plan)
@receiver(pre_save, signal=Expense)
def save_period_time(sender, instance, **kwargs):
	instance.periodtime.save()

