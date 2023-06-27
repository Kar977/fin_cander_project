from django.shortcuts import render
from django.http import HttpResponse
import datetime


def home_view(request):
	current_date = datetime.datetime.now()
	return render(request, "website/home.html", {"current_year": current_date.year, "current_month": current_date.month})
