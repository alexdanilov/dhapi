from rest_framework.serializers import ModelSerializer

from .models import Restaurant


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'opens_at', 'closes_at')
