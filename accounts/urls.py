from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('employer-dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('candidate-dashboard/', views.candidate_dashboard, name='candidate_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]