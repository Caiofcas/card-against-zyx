from rest_framework import routers

from matches.viewsets import MatchViewset

router = routers.DefaultRouter()

router.register("matches", MatchViewset, basename="matches")
