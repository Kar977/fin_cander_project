from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm


class RegisterView(SuccessMessageMixin, CreateView):

	template_name = "users/Register.html"
	success_url = reverse_lazy("login")
	form_class = UserRegisterForm
	success_message = "Your profile was created successfully"
