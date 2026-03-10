from rest_framework import generics, permissions
from rest_framework.response import Response
from django.utils.timezone import now
from django.db.models import Sum

from .models import FoodItem, DietLog
from .serializers import FoodItemSerializer, DietLogSerializer


# List all food items
class FoodListView(generics.ListAPIView):

    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [permissions.IsAuthenticated]


# Log food eaten by user
class AddDietLogView(generics.CreateAPIView):

    serializer_class = DietLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):

        food = serializer.validated_data['food']
        quantity = serializer.validated_data['quantity_grams']

        calories = (food.calories_per_100g / 100) * quantity
        protein = (food.protein_per_100g / 100) * quantity
        carbs = (food.carbs_per_100g / 100) * quantity
        fat = (food.fat_per_100g / 100) * quantity

        serializer.save(
            user=self.request.user,
            calories=calories,
            protein=protein,
            carbs=carbs,
            fat=fat
        )


# Get today's meals
class TodayDietView(generics.ListAPIView):

    serializer_class = DietLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        today = now().date()

        return DietLog.objects.filter(
            user=self.request.user,
            date=today
        )


# Daily nutrition summary
class DietSummaryView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        today = now().date()

        logs = DietLog.objects.filter(
            user=request.user,
            date=today
        )

        summary = logs.aggregate(
            total_calories=Sum('calories'),
            total_protein=Sum('protein'),
            total_carbs=Sum('carbs'),
            total_fat=Sum('fat')
        )

        return Response({
            "calories_consumed": summary['total_calories'] or 0,
            "protein_consumed": summary['total_protein'] or 0,
            "carbs_consumed": summary['total_carbs'] or 0,
            "fat_consumed": summary['total_fat'] or 0
        })