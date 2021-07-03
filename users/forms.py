from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib import messages

from .models import UserProfile


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True,
                                label='Password', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html()
                                )
    password2 = forms.CharField(required=True,
                                label='Repeat password', widget=forms.PasswordInput,
                                )

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password_validation.validate_password(password1)

        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают', code='password_mismatch'
            )}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        if commit:
            user.save()
        return user

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)