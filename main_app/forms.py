from django.forms import ModelForm
<<<<<<< HEAD
from .models import Job, Platform
=======
from .models import Job, Status
>>>>>>> develop

class JobForm(ModelForm):
  class Meta:
    model = Job
    fields = ['title', 'pay_range', 'company', 'notes', 'job_details', 'platform', 'status', 'resume_groomed']

<<<<<<< HEAD
class PlatformForm(ModelForm):
  class Meta:
    model = Platform
=======
class StatusForm(ModelForm):
  class Meta:
    model = Status
>>>>>>> develop
    fields = '__all__'
