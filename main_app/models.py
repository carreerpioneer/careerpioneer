from django.db import models
import uuid 

class Job(models.Model):
  title = models.CharField(max_length=200)
  pay_range = models.CharField(max_length=200, null=True, blank=True)
  company = models.CharField(max_length=200)
  notes = models.TextField(null=True, blank=True)
  # owner = models.
  # status = 
  resume_groomed = models.BooleanField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

  def __str__(self):
    return self.title

class JobDetails(models.Model):
  location = models.CharField(max_length=200)
  remote = models.BooleanField()
  job = models.ForeignKey(Job, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title

class Platform(models.Model):
  name = models.CharField(max_length=100)
  website = models.CharField(max_length=100)
  job = models.ForeignKey(Job, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

  def __str__(self):
      return self.name

