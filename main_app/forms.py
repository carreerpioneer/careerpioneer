from django.forms import ModelForm
from .models import Job, Status

class JobForm(ModelForm):
  class Meta:
    model = Job
    fields = '__all__'

class StatusForm(ModelForm):
  class Meta:
    model = Status
    fields = '__all__'