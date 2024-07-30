from django import forms
from .models import Receiver, Contract

PROVINCES = [
    ('B', 'Bukhara'),
    ('S', 'Samarkand'),
    ('T', 'Tashkent'),
    ('A', 'Andijan'),
    ('D', 'Djizak'),
    ('K', 'Kashkadarya'),
    ('NM', 'Namangan'),
    ('N', 'Navoi'),
    ('SU', 'Surhandarya'),
    ('SI', 'Sirdarya'),
    ('F', 'Fergana'),
    ('H', 'Horezm'),
    ('KA', 'Karakalpakstan'),
]


class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = ['name', 'phone', 'province', 'street', 'home_number']
        widgets = {
            'province': forms.Select(choices=PROVINCES),
        }


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = (
            'name', 'last_name', 'patronymic', 'number', 'company_name', 'position', 'city', 'address', 'description',
            'size', )
