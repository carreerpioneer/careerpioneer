from django import forms
from django.forms import ModelForm
from .models import Job, Platform, Status, JobDetail

class JobForm(forms.ModelForm):
  class Meta:
    model = Job
    fields = ['title', 'company', 'platform', 'url', 'pay_range', 'job_details', 'status', 'resume_groomed', 'notes']

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'company': forms.TextInput(attrs={'class': 'form-control'}),
      'platform': forms.Select(attrs={'class': 'form-control'}),
      'url': forms.TextInput(attrs={'class': 'form-control'}),
      'pay_range': forms.TextInput(attrs={'class': 'form-control'}),
      'job_details': forms.Select(attrs={'class': 'form-control'}),
      'status': forms.Select(attrs={'class': 'form-control'}),
      'resume_groomed': forms.CheckboxInput(),
      'notes': forms.Textarea(attrs={'class': 'form-control'}),
    }


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
