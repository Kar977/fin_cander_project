import datetime

from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        current_date = datetime.datetime.now()
        return render(
            request,
            "website/home.html",
            {"current_year": current_date.year, "current_month": current_date.month},
        )
