from django import forms

from website.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        exclude = ["subscription_date"]

    def save(self, *args, **kwargs):
        m = super().save(commit=False)
        email = Email.objects.create(name=m.name, email=m.email)
        print("\n\n\nw form save\n\n\n", flush=True)
        return email
