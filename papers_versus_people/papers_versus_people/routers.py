from rest_framework import routers

from cards.viewsets import CardSetViewset
from matches.viewsets import MatchViewset

router = routers.DefaultRouter()

router.register("card_sets", CardSetViewset, basename="card_sets")
router.register("matches", MatchViewset, basename="matches")
