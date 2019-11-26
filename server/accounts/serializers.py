from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.serializers import ReviewSerializer


class UserSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'review_set')