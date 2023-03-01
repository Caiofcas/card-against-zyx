from rest_framework import routers

from cards.viewsets import CardViewset

router = routers.DefaultRouter()
router.register(prefix="cards/", viewset=CardViewset, basename="cards")
