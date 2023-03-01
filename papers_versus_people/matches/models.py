import random

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres import fields
from model_utils.models import TimeStampedModel

from cards.models import Card


User = get_user_model()


class PlayerInMatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey("Match", on_delete=models.CASCADE)
    hand = models.ManyToManyField("cards.Card")

    @property
    def is_czar(self) -> bool:
        return self.match.current_czar.id == self.id

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("user", "match"),
                name="user_can_only_be_in_match_once",
            ),
        ]


class Match(TimeStampedModel):
    available_sets = models.ManyToManyField("cards.CardSet")
    players = models.ManyToManyField(User, through="PlayerInMatch")

    czar_order = fields.ArrayField(models.PositiveIntegerField())
    current_czar_idx = models.PositiveSmallIntegerField(default=0)

    current_round = models.PositiveSmallIntegerField(default=1)
    max_rounds = models.PositiveSmallIntegerField(default=200)

    current_black_card = models.ForeignKey("cards.Card", on_delete=models.CASCADE)
    previous_black_cards = fields.ArrayField(
        models.PositiveIntegerField(),
        default=list,
    )

    @property
    def current_czar(self):
        return self.players.get(id=self.czar_order[self.current_czar_idx])

    def go_to_next_round(self) -> bool:
        """Returns if should continue match"""

        # increment round counter
        self.current_round += 1

        if self.finish_match():
            return False

        # change czar
        self.current_czar_idx = (
            self.current_czar_idx + 1
        ) % len(self.czar_order)

        # change black card
        next_card = random.choice(
            Card.objects
                .filter(sets__in=self.available_sets)
                .exclude(id__in=self.previous_black_cards)
        )
        self.previous_black_cards.append(self.current_black_card)
        self.current_black_card = next_card

        self.save()

        return True
