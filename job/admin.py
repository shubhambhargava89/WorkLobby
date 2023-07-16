from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(StudentUser)

admin.site.register(Recruiter)

admin.site.register(Job)

admin.site.register(ApplyJob)

admin.site.register(Ticket)

admin.site.register(Feedback)

admin.site.register(Notification)
