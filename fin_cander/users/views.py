from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView

from users.forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from users.models import Profile, User


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"
    print(success_message)


class ProfileView(LoginRequiredMixin, generic.View):
    model = Profile
    template_name = "users/profile.html"

    def get(self, request, user_name):
        user_object = User.objects.get(username=user_name)
        user_related_data = Profile.objects.get(user=user_object)
        context = {"user_related_data": user_related_data}
        return render(request, self.template_name, context)


# TODO przerobić tą funkcje na klase
@login_required
def profile(request, **kwargs):

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        password_form = PasswordChangeForm(request.user, request.POST)

        if user_form.is_valid() and profile_form.is_valid() and password_form.is_valid():
            user_form.save()
            profile_form.save()

            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your profile been updated")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        password_form = PasswordChangeForm(request.user)

    return render(request, "users/profile.html", {"user_form": user_form, "profile_form": profile_form, "password_form": password_form})
