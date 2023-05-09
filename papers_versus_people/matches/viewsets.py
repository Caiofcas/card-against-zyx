from rest_framework import viewsets, mixins, permissions

from .models import Match
from .serializers import MatchSerializer


class MatchViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
    permission_classes = []
    # TODO: enable permissions
    # permission_classes = [permissions.IsAuthenticated, ]
