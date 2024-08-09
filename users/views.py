from django import forms
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm, EditProfileForm, ResetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from urllib.parse import urlencode

from delivery.models import qr


# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            qr_instance = qr.objects.create(name=user)
            qr_instance.save()
            # Log the user in

            # Send confirmation email   x
            subject = 'Welcome to My Site'
            message = f'Hi {user.username},\n\nThank you for registering at our site.\n\nBest regards,\nYour Site Team'
            from_email = 'setora087@gmail.com'
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)

            return redirect('users:sign_in')  # Redirect to a success page
    else:
        form = SignUpForm()

    return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    language = request.GET.get('language', 'en')  # Default to 'en' if no language is specified
    google_oauth2_url = get_google_oauth2_url(language)
    form = SignInForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('delivery:home')

    return render(request, 'sign_in.html', {
        'form': form,
        'google_oauth2_url': google_oauth2_url
    })

def get_google_oauth2_url(language):
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    redirect_uris = {
        'en': "http://127.0.0.1:8000/en/accounts/google/login/callback/",
        'ru': "http://127.0.0.1:8000/ru/accounts/google/login/callback/",
    }
    params = {
        "client_id": "831062076834-7sc66pt8tquu0mhjv9919v85ivu52sa6.apps.googleusercontent.com",  # Your Google Client ID
        "redirect_uri": redirect_uris[language],  # Select the correct redirect URI based on the language
        "scope": "email profile",
        "response_type": "code",
        "state": "some_random_state",  # You can generate a random state for security purposes
        "access_type": "online",
        "code_challenge_method": "S256",
        "code_challenge": "dwLXrNlDJdwEbdwGp_bduS5CnScPwBEeWkZB_dXttA0",  # Your code challenge if you are using PKCE
        "flowName": "GeneralOAuthFlow",
    }
    url = f"{base_url}?{urlencode(params)}"
    return url


def sign_out(request):
    logout(request)
    return redirect('delivery:home')


def edit_profile(request):
    form = EditProfileForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Profile has been edited successfully')
        return redirect('delivery:home')
    return render(request, 'edit_profile.html', {'form': form})


def reset_password(request):
    form = ResetPasswordForm(request.user, request.POST)

    if form.is_valid() and request.method == 'POST':
        user = form.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Password has been reset successfully')
        return redirect('delivery:home')
    form = ResetPasswordForm(request.user)
    return render(request, 'reset_password.html', {'form': form})


def redirect_view(request):
    return render(request, 'redirect.html')
