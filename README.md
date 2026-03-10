Fitness Health Tracker API

Backend API for a Fitness Health Tracker application.
This system allows users to:

Register and login securely using JWT authentication

Manage personal fitness profile

Track daily workouts

Log diet and nutrition intake

View calorie and macronutrient summaries

Base URL
http://127.0.0.1:8000/api/
Authentication

Authentication is done using JWT tokens.

After login, include this header in protected requests:

Authorization: Bearer <access_token>
1. Register User
Endpoint
POST /Users/register/
Input
{
 "username": "sailendra",
 "email": "sailendra@gmail.com",
 "password": "StrongPass123",
 "confirm_password": "StrongPass123"
}
Response
{
 "message": "User registered successfully",
 "user": {
  "id": 1,
  "username": "sailendra",
  "email": "sailendra@gmail.com"
 }
}
2. Login User
Endpoint
POST /Users/login/
Input
{
 "username": "sailendra",
 "password": "StrongPass123"
}
Response
{
 "refresh": "REFRESH_TOKEN",
 "access": "ACCESS_TOKEN"
}
3. Refresh Access Token
Endpoint
POST /token/refresh/
Input
{
 "refresh": "REFRESH_TOKEN"
}
Response
{
 "access": "NEW_ACCESS_TOKEN"
}
Profile Module

Stores user fitness details.

4. Create / Update Profile
Endpoint
POST /Users/profile/
Headers
Authorization: Bearer ACCESS_TOKEN
Input
{
 "age": 21,
 "height": 175,
 "weight": 70,
 "gender": "m",
 "daily_calorie_goal": 2200,
 "goal":"gain"
}
Response
{
 "message": "Profile saved successfully"
}
6. View Profile
Endpoint
GET /Users/profile/
Headers
Authorization: Bearer ACCESS_TOKEN
Response
{
 "user": "sailendra",
 "age": 22,
 "height": 175,
 "weight": 70,
 "gender": "male",
 "daily_calorie_goal": 2200
}
Workout Module

Tracks workouts assigned to users.

6. List All Workouts
Endpoint
GET /workouts/templates/
Response
[
 {
  "id": 1,
  "title": "Push Ups",
  "workout_type": "arms",
  "average_duration_minutes": 10,
  "average_calories_burn": 80
 }
]
7. Assign Workout to User
Endpoint
POST /Workouts/assign/
Headers
Authorization: Bearer ACCESS_TOKEN
Input
{
 "workout": 1,
 "actual_duration":30
}
Response
{
 "message": "Workout assigned",
 "status": "pending"
}
9. Get Today's Workouts
Endpoint
GET /Workouts/today/
Headers
Authorization: Bearer ACCESS_TOKEN
Response
[
 {
  "workout": "Push Ups",
  "status": "pending",
  "date_assigned": "2026-03-10"
 }
]
10. Complete Workout
Endpoint
PATCH /Workouts/complete/{id}/
Headers
Authorization: Bearer ACCESS_TOKEN
Input
{
 "status": "completed"
}
Response
{
 "status": "completed"
}
Diet Module

Tracks nutrition intake.

10. Get All Food Items
Endpoint
GET /Diet/foods/
Response
[
 {
  "id": 1,
  "name": "Rice",
  "calories_per_100g": 130,
  "protein_per_100g": 2,
  "carbs_per_100g": 28,
  "fat_per_100g": 0
 }
]
11. Log Food Intake
Endpoint
POST /Diet/log/
Headers
Authorization: Bearer ACCESS_TOKEN
Input
{
 "food": 1,
 "quantity_grams": 200,
 "meal_type": "lunch"
}
Response
{
 "food": "Rice",
 "quantity_grams": 200,
 "calories": 260,
 "protein": 4,
 "carbs": 56,
 "fat": 0
}
12. Get Today's Diet
Endpoint
GET /Diet/today/
Headers
Authorization: Bearer ACCESS_TOKEN
Response
[
 {
  "food": "Egg",
  "meal_type": "breakfast",
  "quantity_grams": 100,
  "calories": 155
 }
]
13. Diet Summary
Endpoint
GET /Diet/summary/
Headers
Authorization: Bearer ACCESS_TOKEN
Response
{
 "calories_consumed": 1200,
 "protein_consumed": 60,
 "carbs_consumed": 150,
 "fat_consumed": 30
}
Technologies Used

Python

Django

Django REST Framework

JWT Authentication using Simple JWT

SQLite / MySQL

Features

Secure JWT authentication

Workout tracking

Diet logging

Nutrition calculation

User fitness profile management
