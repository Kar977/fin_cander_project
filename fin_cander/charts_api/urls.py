from django.urls import path
from .views import GetPeriodData
from django.contrib.auth import views as auth_views

urlpatterns = [
	path("income/", GetPeriodData.as_view())
]

# /api/income?year=XXX&month=XXX)
