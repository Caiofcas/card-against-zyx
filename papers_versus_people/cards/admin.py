from django.contrib import admin

from .models import Card, CardSet


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    ...


@admin.register(CardSet)
class CardSetAdmin(admin.ModelAdmin):
    ...
