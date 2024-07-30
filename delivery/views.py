from django.shortcuts import render, redirect
from .models import qr
from .forms import ReceiverForm, ContractForm
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_backends


# Create your views here.

def home(request):
    return render(request, 'home.html')


def test(request):
    photos = qr.objects.all()
    return render(request, 'test.html', {'photos': photos})


def calc(request):
    return render(request, 'calculate.html')


def deliverer(request):
    if request.method == 'POST':
        form = ReceiverForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            province = form.cleaned_data['province']
            street = form.cleaned_data['street']
            home_number = form.cleaned_data['home_number']

            return redirect('delivery:deliverer')
    else:
        form = ReceiverForm()

    return render(request, 'deliverer.html', {'form': form})


def contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            patronymic = form.cleaned_data['patronymic']
            number = form.cleaned_data['number']
            company_name = form.cleaned_data['company_name']
            position = form.cleaned_data['position']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            description = form.cleaned_data['description']
            size = form.cleaned_data['size']
            return redirect('delivery:contract')
    else:
        form = ContractForm()

    return render(request, 'contract.html', {'form': form})


