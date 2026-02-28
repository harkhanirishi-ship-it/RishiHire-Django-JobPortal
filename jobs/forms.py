from django import forms
from .models import Job
from .models import Application

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'salary', 'description']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'email', 'gender', 'resume', 'cover_letter']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write something...'}),
        }
        