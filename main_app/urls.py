from hashlib import pbkdf2_hmac
from django.urls import path
from . import views

urlpatterns = [
  path('', views.get_jobs, name='jobs'),
  path('job/<str:pk>/', views.jobDetails, name='job-details'),
]