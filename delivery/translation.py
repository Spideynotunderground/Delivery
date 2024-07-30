from modeltranslation.translator import register, TranslationOptions
from .models import Receiver, Contract


@register(Receiver)
class ReceiverTranslationOptions(TranslationOptions):
    fields = ('name', 'phone', 'province', 'street', 'home_number')


@register(Contract)
class ContractTranslationOptions(TranslationOptions):
    fields = (
        'name', 'last_name', 'patronymic', 'number', 'company_name', 'position', 'city', 'address', 'description',
        'size')
