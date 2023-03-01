from rest_framework import serializers

from .models import Card, CardSet


class CardSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardSet
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    sets = serializers.ListField(child=CardSetSerializer(), allow_empty=False)

    class Meta:
        model = Card
        fields = "__all__"

    def create(self, validated_data):
        return Card.objects.create(
            **validated_data,
            sets=[
                CardSet.objects.get_or_create(**set)[0]
                for set in validated_data.pop("sets")
            ]
        )
