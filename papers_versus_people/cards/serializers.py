from rest_framework import serializers

from .models import Card, CardSet


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"

    def create(self, validated_data):
        return Card.objects.create(
            **validated_data,
            sets=[
                CardSet.objects.get_or_create(name=set_name)[0]
                for set_name in validated_data.pop("sets")
            ]
        )
