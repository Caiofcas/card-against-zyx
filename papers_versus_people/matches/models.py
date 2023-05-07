import random

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres import fields
from model_utils.models import TimeStampedModel

from cards.models import Card, CARD_COLORS

HAND_SIZE = 7

User = get_user_model()


class PlayerInMatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey("Match", on_delete=models.CASCADE)
    hand = models.ManyToManyField("cards.Card")
    played_card = models.ForeignKey(
        "cards.Card",
        default=None,
        null=True,
        on_delete=models.PROTECT,
        related_name="played_by_player",
    )

    score = models.IntegerField(default=0)

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

    winning_score = models.PositiveSmallIntegerField(default=7)
    winner = models.OneToOneField(
        "PlayerInMatch",
        default=None,
        null=True,
        on_delete=models.CASCADE,
        related_name="winning_match",
    )

    current_black_card = models.ForeignKey("cards.Card", on_delete=models.PROTECT)
    previous_black_cards = fields.ArrayField(
        models.PositiveIntegerField(),
        default=list,
    )

    @property
    def current_czar(self):
        return self.players.get(id=self.czar_order[self.current_czar_idx])

    def possible_cards(self, color: CARD_COLORS = CARD_COLORS.white):
        return Card.objects.filter(sets__in=self.available_sets, color=color)

    def go_to_next_round(self) -> bool:
        """Returns if should continue match"""

        # increment round counter
        self.current_round += 1

        if self.current_round >= self.max_rounds:
            return False

        # change czar
        self.current_czar_idx = (self.current_czar_idx + 1) % len(self.czar_order)

        # change black card
        next_card = random.choice(
            self.possible_cards(CARD_COLORS.black).exclude(
                id__in=self.previous_black_cards
            )
        )
        self.previous_black_cards.append(self.current_black_card)
        self.current_black_card = next_card

        self.save()

        return True

    def update_player_hands(self):
        possible_cards = list(
            self.possible_cards().exclude(
                id__in=[i for player in self.players for i in player.hand]
            )
        )

        for player in self.players:
            player: PlayerInMatch

            if player.is_czar:
                continue

            new_card = possible_cards.pop(random.uniform(0, len(possible_cards)))
            player.hand.delete(player.played_card)
            player.hand.add(new_card)

    def start_match(self):
        self.current_round = 1
        self.winner = None
        self.current_czar_idx = 0

        number_of_players = self.players.count()

        self.czar_order = random.sample(range(number_of_players), number_of_players)

        hands = random.sample(self.possible_cards(), number_of_players * HAND_SIZE)
        for i, player in enumerate(self.players):
            player: PlayerInMatch

            player.hand.set(hands[:HAND_SIZE])
            hands = hands[HAND_SIZE:]

        self.save()
