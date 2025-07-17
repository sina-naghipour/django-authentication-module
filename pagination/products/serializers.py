from rest_framework import serializers


class ReviewSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    stars     = serializers.IntegerField()
    content   = serializers.CharField()

class ProductSerializer(serializers.Serializer):
    uuid          = serializers.UUIDField()
    name          = serializers.CharField()
    description   = serializers.CharField()
    owner         = serializers.CharField()
    quantity      = serializers.IntegerField()
    rating        = serializers.ReadOnlyField()
    reviews       = ReviewSerializer(many=True, read_only=True)