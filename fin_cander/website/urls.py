from django.urls import path

from website.views import HomeView

urlpatterns = [
	path("home/", HomeView.as_view(), name="home_site")
]
