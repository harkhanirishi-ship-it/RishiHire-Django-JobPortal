from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post-job/', views.post_job, name='post_job'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('create-job/', views.create_job, name='create_job'),
    path('jobs/', views.job_list, name='job_list'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path('my-jobs/', views.my_jobs, name='my_jobs'),
    path('applications/<int:job_id>/', views.view_applications, name='view_applications'),
    path('jobs/', views.all_jobs, name='all_jobs'),
]