from django.contrib import admin
from .models import qr, Receiver, Contract
from modeltranslation.admin import TranslationAdmin

# Register your models here.

admin.site.register(qr)


@admin.register(Receiver)
class ReceiverAdmin(TranslationAdmin):
    ...


@admin.register(Contract)
class ContractAdmin(TranslationAdmin):
    ...

