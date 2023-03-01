from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices


CARD_COLORS = Choices((0, "black", _("black")), (1, "white", _("white")))


class CardSet(models.Model):
    name = models.CharField(max_length=200)


class Card(models.Model):
    text = models.TextField()
    sets = models.ManyToManyField(CardSet, related_name="cards")
    color = models.PositiveSmallIntegerField(choices=CARD_COLORS)
