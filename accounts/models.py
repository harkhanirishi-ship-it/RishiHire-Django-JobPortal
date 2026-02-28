from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE = (
        ('employer', 'Employer'),
        ('candidate', 'Candidate'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE)

class Profile(models.Model):
    candidate = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField()
    skills = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    is_recruiter = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
