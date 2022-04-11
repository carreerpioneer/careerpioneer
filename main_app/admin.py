from django.contrib import admin
from .models import Job, JobDetail, Platform

admin.site.register(Job)
admin.site.register(JobDetail)
admin.site.register(Platform)