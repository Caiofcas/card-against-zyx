from rest_framework import viewsets, mixins

from .models import CardSet
from .serializers import CardSetSerializer


class CardSetViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CardSetSerializer
    queryset = CardSet.objects.all()
    permission_classes = []
    # TODO: enable permissions
    # permission_classes = [permissions.IsAuthenticated, ]
