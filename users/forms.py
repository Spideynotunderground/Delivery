from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django_recaptcha.fields import ReCaptchaField
from django.conf import settings


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Create username')
    email = forms.EmailField(label='Write email')
    password1 = forms.CharField(
        widget=forms.PasswordInput(), label='Create password')
    password2 = forms.CharField(
        widget=forms.PasswordInput(), label='Repeat password')
    recaptcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox,
        error_messages={
            'required': settings.RECAPTCHA_ERROR_MSG['required']
        }
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class SignInForm(AuthenticationForm):
    username = forms.CharField(label='Write username')
    password = forms.CharField(
        widget=forms.PasswordInput(), label='Write password')

    class Meta:
        model = User
        fields = ('username', 'password')


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email address')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ResetPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(), label='Old password')
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(), label='Create new password')
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(), label='Repeat new password')

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
