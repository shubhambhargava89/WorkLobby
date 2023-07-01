"""pms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name="index"),
                  path('admin_login', admin_login, name="admin_login"),
                  path('admin_home', admin_home, name='admin_home'),
                  path('recruiter_login', recruiter_login, name="recruiter_login"),
                  path('recruiter_signup', recruiter_signup, name="recruiter_signup"),
                  path('recruiter_home', recruiter_home, name="recruiter_home"),
                  path('user_login', user_login, name="user_login"),
                  path('user_signup', user_signup, name="user_signup"),
                  path('user_home', user_home, name="user_home"),
                  path('Logout', Logout, name="Logout"),
                  path('view_users', view_users, name="view_users"),
                  path('add_job', add_job, name="add_job"),
                  path('edit_job/<int:pid>', edit_job, name="edit_job"),
                  path('change_companylogo/<int:pid>', change_companylogo, name="change_companylogo"),
                  path('delete_job/<int:pid>', delete_job, name="delete_job"),
                  path('job_list',job_list, name="job_list"),
                  path('delete_user/<int:pid>', delete_user, name="delete_user"),
                  path('delete_recruiter/<int:pid>', delete_recruiter, name="delete_recruiter"),
                  path('view_recruiters', view_recruiters, name="view_recruiters"),
                  path('recruiter_pending', recruiter_pending, name="recruiter_pending"),
                  path('recruiter_accept', recruiter_accept, name="recruiter_accept"),
                  path('recruiter_reject', recruiter_reject, name="recruiter_reject"),
                  path('change_status/<int:pid>', change_status, name="change_status"),
                  path('change_passworduser', change_passworduser, name="change_passworduser"),
                  path('change_passwordadmin', change_passwordadmin, name="change_passwordadmin"),
                  path('change_passwordrecruiter', change_passwordrecruiter, name="change_passwordrecruiter"),
                  path('latest_jobs', latest_jobs, name="latest_jobs"),
                  path('user_joblist', user_joblist, name="user_joblist"),
                  path('job_detail/<int:pid>', job_detail, name="job_detail"),
                  path('applyforjob/<int:pid>', applyforjob, name="applyforjob"),
                  path('applied_candidatelist',applied_candidatelist,name="applied_candidatelist"),
    path('contact',contact,name="contact"),
path('admin_job', admin_job, name="admin_job"),
path('admin_job_detail/<int:pid>', admin_job_detail, name="admin_job_detail"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
