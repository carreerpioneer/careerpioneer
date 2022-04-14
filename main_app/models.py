from django.db import models
from django.contrib.auth.models import User
import uuid 

class JobDetail(models.Model):
  location = models.CharField(max_length=200)
  remote = models.BooleanField()
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.location

class Platform(models.Model):
  name = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Status(models.Model):
  name = models.CharField(max_length=250)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Job(models.Model):
  title = models.CharField(max_length=200)
  pay_range = models.CharField(max_length=200, null=True, blank=True)
  company = models.CharField(max_length=200)
  notes = models.TextField(null=True, blank=True)
  job_details = models.ForeignKey(JobDetail, on_delete=models.CASCADE, default='')
  platform = models.ForeignKey(Platform, on_delete=models.CASCADE, default='')
  status = models.ForeignKey(Status, on_delete=models.CASCADE, default='')
  resume_groomed = models.BooleanField()
  url = models.CharField(max_length=500, null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title


