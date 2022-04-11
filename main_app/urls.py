from hashlib import pbkdf2_hmac
from django.urls import path
from . import views

urlpatterns = [
  path('', views.get_jobs, name='jobs'),
  path('job/<str:pk>/', views.jobDetails, name='job-details'),
  path('create-job/', views.create_job, name="create-job"),
  path('update-job', views.update_job, name='update-job'),
  path('delete-job', views.delete_job, name='delete-job'),
]