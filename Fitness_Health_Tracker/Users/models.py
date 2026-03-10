from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    GOAL_CHOICES = (
        ('lose', 'Lose Weight'),
        ('gain', 'Gain Muscle'),
        ('maintain', 'Maintain Weight'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)  # in meters
    weight = models.FloatField(null=True, blank=True)  # in kg
    goal = models.CharField(max_length=10, choices=GOAL_CHOICES, null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Auto calculate BMI
        if self.height and self.weight:
            self.bmi = self.weight / (self.height ** 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username