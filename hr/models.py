#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default
# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length = 100)
    department_manager = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.department_name

class Employee_extra(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    sex = models.CharField(max_length = 100)
    email = models.EmailField()
    department = models.ForeignKey(Department)
    position = models.CharField(max_length = 100)
    base_salary = models.FloatField()
    extra_salary = models.FloatField(default=0)
    hiredate = models.DateField()
    pic = models.ImageField(upload_to='upload')
    class Meta:
        permissions = (('department_manager','department_manager'),
                       ('personnel_assistant','personnel_assistant'),
                       ('personnel_manager','personnel_manager'),
                       ('admin','admin'),
                       )
    
    
class Attendence(models.Model):
    attendence_name = models.CharField(max_length = 100)
    is_early_or_late = models.BooleanField()
    attendence_date = models.DateField()

class Salary(models.Model):
    name = models.CharField(max_length = 100)
    year = models.CharField(max_length = 100)
    month = models.CharField(max_length = 100)
    salary = models.FloatField()
    
class Announce(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date = models.DateField()
    def __unicode__(self):
        return self.title 
