from rest_framework import serializers
from core.models import Post, Review
from accounts.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    rating = serializers.ReadOnlyField()
    author = UserSerializer()
    class Meta:
        model            = Post
        fields           = ['uuid', 'title', 'content']
        read_only_fields = ['uuid']



class Review(serializers.ModelSerializer):
    author = UserSerializer()
    post   = PostSerializer()
    stars  = serializers.IntegerField(min_value=1, max_value=5)
    class Meta:
        model  = Review
        fields = ['__all__']