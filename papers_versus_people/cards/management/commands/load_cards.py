import argparse
import json
from typing import Any, Optional, TypedDict

from django.core.management.base import BaseCommand, CommandParser

from cards.models import CardSet, Card, CARD_COLORS


class RawWhiteCard(TypedDict):
    text: str
    pack: int


class RawBlackCard(RawWhiteCard):
    pick: int


class RawCardSet(TypedDict):
    name: str
    white: list[RawWhiteCard]
    black: list[RawBlackCard]
    official: bool


# TODO: add some cli feedback
class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "file", type=argparse.FileType("r"), help="json file containing card data"
        )
        return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        file = options.pop("file")
        data: list[RawCardSet] = json.load(file)

        for raw_set in data:
            cardset, _ = CardSet.objects.get_or_create(
                name=raw_set["name"],
                defaults={"official": raw_set["official"]},
            )

            for raw_card in raw_set["white"]:
                c, _ = Card.objects.get_or_create(
                    text=raw_card["text"],
                    color=CARD_COLORS.white,
                )
                c.sets.add(cardset)

            for raw_card in raw_set["black"]:
                c, _ = Card.objects.get_or_create(
                    text=raw_card["text"],
                    color=CARD_COLORS.black,
                )
                c.sets.add(cardset)
