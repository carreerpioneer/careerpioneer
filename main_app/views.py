from django.shortcuts import render
from django.http import HttpResponse

job_list = [
  {
    "id": 1,
    "title": "Super Senior Dev",
    "status": "Applied",
  },
  {
    "id": 2,
    "title": "Super Junior Dev",
    "status": "Applied",
  },
  {
    "id": 3,
    "title": "Super Senior Dev",
    "status": "Not Applied",
  },
]

def jobs(request):
  context = {'jobs': job_list}
  print(context)
  return render(request, "jobs/jobs.html", context)

def jobDetails(request, pk):
  print(pk)
  return HttpResponse("<h1>Job Details Page + ' ' + {{pk}}</h1>")

