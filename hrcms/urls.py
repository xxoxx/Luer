"""hrcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','hr.views.index'),
    url(r'^accounts/login/$','hr.views.login_page'),
    url(r'^accounts/logout$','hr.views.logout'),
    url(r'^logout$',logout),
    url(r'^default$','hr.views.default'),
    url(r'^extra_lock$','hr.views.extra_lock'),
    url(r'^info$','hr.views.info'),
    url(r'^info_single$','hr.views.info_single'),
    url(r'^info_department$','hr.views.info_department'),
    url(r'^attendence_cal$','hr.views.attendence_cal'),
    url(r'^attendence_cal_department$','hr.views.attendence_cal_department'),
    url(r'^attendence_cal_single$','hr.views.attendence_cal_single'),
    url(r'^attendence_result$','hr.views.attendence_result'),
    url(r'^attendence_result_department$','hr.views.attendence_result_department'),
    url(r'^attendence_result_single$','hr.views.attendence_result_single'),
    url(r'^attendence$','hr.views.attendence'),
    url(r'^insert_attendence$','hr.views.insert_attendence'),
    url(r'^salary_cal$','hr.views.salary_cal'),
    url(r'^salary_history$','hr.views.salary_history'),
    url(r'^sign_print$','hr.views.sign_print'),
    url(r'^search$','hr.views.search'),
    url(r'^sqli$','hr.views.sqli'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
