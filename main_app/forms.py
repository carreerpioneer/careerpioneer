from django.forms import ModelForm
from .models import Job

class JobForm(ModelForm):
  class Meta:
    model = Job
    fields = ['title', 'pay_range', 'company', 'notes', 'job_details', 'platform', 'status', 'resume_groomed']