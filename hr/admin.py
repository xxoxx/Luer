#coding:utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from hr.models import Department,Employee_extra,Attendence,Announce


class Employee_extraInline(admin.StackedInline):
    model = Employee_extra
    can_delete = False
    verbose_name_plural = 'employee_extra'

    
class UserAdmin(UserAdmin):
    inlines = (Employee_extraInline,)
    
    
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name','department_manager']
    
    
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ['attendence_name','is_early_or_late','attendence_date']
    
class AnnounceAdmin(admin.ModelAdmin):
    list_display = ['title','content','date']
    


# Register your models here.




admin.site.register(Department,DepartmentAdmin)
admin.site.register(Attendence,AttendenceAdmin)
admin.site.register(Announce,AnnounceAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)