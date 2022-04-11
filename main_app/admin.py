from django.contrib import admin
from .models import Job, Platform, JobDetails

admin.site.register(Job)
admin.site.register(Platform)
admin.site.register(JobDetails)