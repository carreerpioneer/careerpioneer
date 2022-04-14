from django import forms
from django.forms import ModelForm, Form
from .models import Job, Platform, Status, JobDetail

class JobForm(ModelForm):
  class Meta:
    model = Job
    fields = ['title', 'company', 'platform', 'url', 'pay_range', 'job_details', 'status', 'resume_groomed', 'notes']

class PlatformForm(ModelForm):
  class Meta:
    model = Platform
    fields = ['name']

class StatusForm(ModelForm):
  class Meta:
    model = Status
    fields = ['name']

class JobDetailForm(ModelForm):
  class Meta:
    model = JobDetail
    fields = ['location', 'remote']
