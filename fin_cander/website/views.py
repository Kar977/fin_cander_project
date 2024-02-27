import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from website.forms import EmailForm


class HomeView(View):
    def get(self, request):
        current_date = datetime.datetime.now()
        email_form = EmailForm()
        return render(
            request,
            "website/home.html",
            {"current_year": current_date.year, "current_month": current_date.month, "email_form": email_form},
        )

    def post(self, request):
        email_form = EmailForm(request.POST)

        return self.process_request(
            request=request,
            email_form=email_form)

    def process_request(self, request, email_form):

        if "email_btn" in request.POST:
            email = email_form.save(commit=False)
            email.subscription_date = datetime.datetime.now()
            email.save()
            messages.success(request, "Subscription successful!")

            print(f"EMAIL ADDED: {email}")

            return redirect("home_site")
