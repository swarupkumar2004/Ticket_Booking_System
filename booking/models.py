from django.db import models
from django.contrib.auth.models import AbstractUser

# Extend the default Django User model if needed (optional)
class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_no = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.service_name} booked by {self.user.first_name} on {self.booking_date} {self.booking_time}"
