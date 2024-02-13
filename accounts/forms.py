from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
 # Make email field optional
    email = forms.EmailField(required=False, help_text='Optional',max_length=254 )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        # email will be saved if provided since it's now optional
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user