from django.forms import ModelForm
from .models import Job, Platform

class JobForm(ModelForm):
  class Meta:
    model = Job
    fields = '__all__'

class PlatformForm(ModelForm):
  class Meta:
    model = Platform
    fields = '__all__'