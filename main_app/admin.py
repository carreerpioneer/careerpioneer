from django.contrib import admin
from .models import Job, JobDetail, Platform, Status

admin.site.register(Job)
admin.site.register(Status)
admin.site.register(JobDetail)
admin.site.register(Platform)