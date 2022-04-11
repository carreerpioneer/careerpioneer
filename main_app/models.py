from django.db import models

# Create your models here.

class Job(models.Model):
  title = models.CharField(max_length=200)
  pay_range = models.CharField(max_length=200, null=True, blank=True)
  company = models.CharField(max_length=200)
  # platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
  notes = models.TextField(null=True, blank=True)
  owner = models.
