from django import forms
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm, EditProfileForm, ResetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log the user in

            # Send confirmation email
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
    form = SignInForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('delivery:home')

    return render(request, 'sign_in.html', {
        'form': form
    })


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
