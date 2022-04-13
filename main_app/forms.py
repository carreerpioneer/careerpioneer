from django.forms import ModelForm
from .models import Job, Platform, Status, JobDetail

class JobForm(ModelForm):
  class Meta:
    model = Job
    fields = ['title', 'pay_range', 'company', 'notes', 'job_details', 'platform', 'status', 'resume_groomed']

class PlatformForm(ModelForm):
  class Meta:
    model = Platform
    fields = '__all__'

class StatusForm(ModelForm):
  class Meta:
    model = Status
    fields = '__all__'

class JobDetailForm(ModelForm):
  class Meta:
    model = JobDetail
    fields = '__all__'
