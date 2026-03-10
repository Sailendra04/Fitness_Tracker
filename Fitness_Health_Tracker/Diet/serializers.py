from rest_framework import serializers
from .models import FoodItem, DietLog


class FoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodItem
        fields = "__all__"


class DietLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = DietLog
        fields = "__all__"
        read_only_fields = ['user', 'calories', 'protein', 'carbs', 'fat', 'date']