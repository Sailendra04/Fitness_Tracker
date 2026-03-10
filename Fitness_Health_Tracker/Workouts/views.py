from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Q
from datetime import date

from .models import WorkoutTemplate, UserWorkout
from .serializers import WorkoutTemplateSerializer, UserWorkoutSerializer


# List all available workout templates
class WorkoutTemplateListView(generics.ListAPIView):
    queryset = WorkoutTemplate.objects.all()
    serializer_class = WorkoutTemplateSerializer
    permission_classes = [IsAuthenticated]


# Assign workout to logged-in user
class AssignWorkoutView(generics.CreateAPIView):
    serializer_class = UserWorkoutSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Get all user workouts (Today on top)
class UserWorkoutListView(generics.ListAPIView):
    serializer_class = UserWorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserWorkout.objects.filter(
            user=self.request.user
        ).order_by('-date_assigned')


# Get Today’s Workout Only
class TodayWorkoutView(generics.ListAPIView):
    serializer_class = UserWorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        today = date.today()
        return UserWorkout.objects.filter(
            user=self.request.user,
            date_assigned=today
        )


# Update Workout Status (Complete Workout)
class CompleteWorkoutView(generics.UpdateAPIView):
    serializer_class = UserWorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserWorkout.objects.filter(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.status = 'completed'
        instance.actual_duration = request.data.get('actual_duration')
        instance.actual_calories_burned = request.data.get('actual_calories_burned')
        instance.completed_at = timezone.now()
        instance.save()

        return Response(
            {"message": "Workout marked as completed"},
            status=status.HTTP_200_OK
        )