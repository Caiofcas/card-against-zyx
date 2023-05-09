from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Match, PlayerInMatch

User = get_user_model()


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            "id",
            "winning_score",
            "available_sets",
        )

    def create(self, validated_data):
        match: Match = super().create(validated_data)

        # TODO: remove when authentication is functional
        user = User.objects.get(username="admin")

        PlayerInMatch.objects.create(
            user=user,
            match=match,
            score=0,
        )

        return match
