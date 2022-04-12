from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/login/', views.Login.as_view(), name='login'),
  path('jobs/', views.get_jobs, name='jobs'),
  path('job/<str:pk>/', views.job_details, name='job-details'),
  path('create-job/', views.create_job, name="create-job"),
  path('update-job/<str:pk>', views.update_job, name='update-job'),
  path('delete-job/<str:pk>', views.delete_job, name='delete-job'),
  path('accounts/signup/', views.signup, name='signup'),
  path('create-platform/', views.create_platform, name="create-platform"),
  path('delete-platform/<str:pk>', views.delete_platform, name='delete-platform'), 
  path('create-status/', views.create_status, name='create-status'),
  path('status/', views.get_status, name='status'),
  path('status/<str:pk>/', views.delete_status, name='delete-status'),
]