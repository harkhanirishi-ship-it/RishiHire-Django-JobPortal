from django.db import models
from django.conf import settings

class Job(models.Model):
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    email = models.EmailField()

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} applied for {self.job.title}"