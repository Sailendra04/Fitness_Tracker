from django.urls import path
from .views import *


urlpatterns = [
    path('foods/', FoodListView.as_view()),
    path('log/', AddDietLogView.as_view()),
    path('today/', TodayDietView.as_view()),
    path('summary/', DietSummaryView.as_view()),
]