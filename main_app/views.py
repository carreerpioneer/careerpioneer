from django.shortcuts import render
from .forms import JobForm
from .models import Job


def get_jobs(request):
  jobs = Job.objects.all()
  context = {'jobs': jobs}
  return render(request, 'jobs/jobs.html', context)

def jobDetails(request, pk):
  job_obj = Job.objects.get(id=pk)
  context = {'job': job_obj}
  return render(request, 'jobs/job-detail.html', context)

def createJob(request):
  pass

