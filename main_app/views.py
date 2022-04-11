from django.shortcuts import render, redirect
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

def create_job(request):
  form = JobForm()

  if request.method == 'POST':
    form = JobForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('jobs')
  
  context = {'form': form}
  return render(request, 'jobs/create-job.html', context)

def update_job(request):
  




