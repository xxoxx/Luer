#coding:utf-8
from hr.models import Department,Employee_extra,Attendence,Salary,Announce
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import time
import datetime
from django.contrib.sessions.models import Session
import re
from django.utils import timezone
# Create your views here.

def default(request):
    announces = Announce.objects.all()
    return render(request,'default.html',locals())
@login_required
def index(request):
    return render(request,'index.html')
def extra_lock(request):
    if request.POST:
        password = request.POST.get('password',None)
        if password == 'unlock':
            return HttpResponseRedirect('/')
    return render(request,'extra_lock.html')
def login_page(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/accounts/login')
        else:
            t = request.session['times']
            print t
            if t >= 5:
                return HttpResponse('想爆破？呵呵，你字典太弱了！！！你ip被哥哥我封了！')
            t += 1
            request.session['times'] = t
            return HttpResponseRedirect('/accounts/login')
    if not request.session.session_key:
        request.session['times'] = 0
    return render(request,'login.html')
            
        
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
def info(request):
    if request.POST:
        name = request.POST.getlist('name')
        sex = request.POST.getlist('sex')
        email = request.POST.getlist('email')
        base_salary = request.POST.getlist('base_salary')
        position = request.POST.getlist('position')
        department_name = request.POST.getlist('department')
        for i in range(len(name)):
            department = Department.objects.get(department_name = department_name[i])
            Employee_extra.objects.filter(name=name[i]).update(sex = sex[i],email = email[i],base_salary = base_salary[i],position = position[i],department = department)
        return HttpResponseRedirect('/')
        
    departments = Department.objects.all()
    employees = Employee_extra.objects.all()
    return render(request,'info.html',locals())
def info_single(request):
    if request.POST:
        password = request.POST.get('password',None)
        request.user.set_password(password)
        name = request.user.employee_extra.name
        Employee_extra.objects.filter(name=name).update(password=password)
        request.user.save()
        return HttpResponseRedirect('/')
    return render(request,'info_single.html')
def info_department(request):
    department = request.user.employee_extra.department
    employees = Employee_extra.objects.all().filter(department=department)
    return render(request,'info_department.html',locals())
def attendence(request):
    employees = Employee_extra.objects.all()
    return render(request,'attendence.html',locals())
def insert_attendence(request):
    attendence_name = request.POST.getlist('attendence_name')
    is_early_or_late = request.POST.getlist('is_early_or_late')
    attendence_date = request.POST.getlist('attendence_date')
    for i in range(len(attendence_name)):
        Attendence.objects.create(attendence_name=attendence_name[i],is_early_or_late=bool(int(is_early_or_late[i])),attendence_date=attendence_date[i]) 
    return HttpResponseRedirect('/')
def attendence_result(request):
    if request.POST:
        department_name = request.POST.get('department',None)
        if department_name == 'all':
            employees = Employee_extra.objects.all()
        else:
            department = Department.objects.filter(department_name=department_name)
            employees = Employee_extra.objects.all().filter(department=department)
        l = []  
        start_date = request.POST.get('start_date',None)
        stop_date = request.POST.get('stop_date',None)
        for e in employees:
            name = e.name
            count = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True).filter(attendence_date__gte=start_date).filter(attendence_date__lte=stop_date).count()
            dates = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True).filter(attendence_date__gte=start_date).filter(attendence_date__lte=stop_date)
            l.append({'name':name,'count':count,'dates':dates})
        return render(request,'attendence_result.html',locals())
def attendence_result_department(request):
    department = request.user.employee_extra.department
    if request.POST:
        l = []
        employees = Employee_extra.objects.all().filter(department=department)
        start_date = request.POST.get('start_date',None)
        stop_date = request.POST.get('stop_date',None)
        for e in employees:
            name = e.name
            count = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True).filter(attendence_date__gte=start_date).filter(attendence_date__lte=stop_date).count()
            dates = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True).filter(attendence_date__gte=start_date).filter(attendence_date__lte=stop_date)
            l.append({'name':name,'count':count,'dates':dates})
        return render(request,'attendence_result.html',locals())
def attendence_result_single(request):
    if request.POST:
        l = []
        name = request.user.employee_extra.name
        start_date = request.POST.get('start_date',None)
        stop_date = request.POST.get('stop_date',None)
        count = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True).filter(attendence_date__gte=start_date).filter(attendence_date__lte=stop_date).count()
        dates = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True).filter(attendence_date__gte=start_date).filter(attendence_date__lte=stop_date)
        l.append({'name':name,'count':count,'dates':dates})
        return render(request,'attendence_result.html',locals())
def attendence_cal(request): 
    l = []
    departments = Department.objects.all()
    employees = Employee_extra.objects.all()
    for e in employees:
            name = e.name
            count = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True).count()
            dates = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True)
            l.append({'name':name,'count':count,'dates':dates})
    

    return render(request,'attendence_cal.html',locals())
        
def attendence_cal_department(request):
    department = request.user.employee_extra.department
    l = []
    employees = Employee_extra.objects.all().filter(department=department)
    for e in employees:
            name = e.name
            count = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True).count()
            dates = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True)
            l.append({'name':name,'count':count,'dates':dates})
    return render(request,'attendence_cal_department.html',locals())
def attendence_cal_single(request):
    l = []
    name = request.user.employee_extra.name
    count = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True).count()
    dates = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True)
    l.append({'name':name,'count':count,'dates':dates})
    return render(request,'attendence_cal_single.html',locals())          
def salary_cal(request):
    l = []
    date = time.strftime('%Y-%m',time.localtime(time.time()))
    start_date = time.strftime('%Y-%m',time.localtime(time.time())) + '-01'
    if time.strftime('%m',time.localtime(time.time())) in [4,6,9,11]:
        stop_date = time.strftime('%Y-%m',time.localtime(time.time())) + '-30'
    elif time.strftime('%m',time.localtime(time.time())) == '2':
        if int(time.strftime('%Y',time.localtime(time.time()))) % 4 == 0:
            stop_date = time.strftime('%Y-%m',time.localtime(time.time())) + '-29'
        else:
            stop_date = time.strftime('%Y-%m',time.localtime(time.time())) + '-28'
    else:
        stop_date = time.strftime('%Y-%m',time.localtime(time.time())) + '-31'
    employees = Employee_extra.objects.all()
    for e in employees:
        name = e.name
        count = Attendence.objects.filter(attendence_name=name).filter(is_early_or_late=True).filter(attendence_date__gte=start_date).filter(attendence_date__lte=stop_date).count()

        if count == 0:
            salary = 200
            e.extra_salary = salary
            e.save()
        elif count >= 3:
            salary = -100
            e.extra_salary = salary
            e.save()
        else:
            salary = 0
            e.extra_salary = salary
            e.save()
 
        salary = e.base_salary + e.extra_salary
        year = time.strftime('%Y',time.localtime(time.time()))
        month = time.strftime('%m',time.localtime(time.time()))
        Salary.objects.create(name=name,month=month,year=year,salary=salary)
        l.append({'name':name,'count':count,'salary':salary})
        
    return render(request,'salary_cal.html',locals())

def salary_history(request):
    if request.POST:
        name = request.POST.get('name',None)
        year = request.POST.get('year',None)
        month = request.POST.get('month',None)
        salary_history = Salary.objects.filter(name=name).filter(year=year).filter(month=month)
        if len(salary_history) == 0:
            salary_history = [{'salary':'没有记录呢',}]
            
        return render(request,'salary_history_result.html',locals())
    employees = Employee_extra.objects.all()
    years = [i for i in range(2015,2021)]
    months = [i for i in range(1,13)]
    return render(request,'salary_history.html',locals())

def sign_print(request):
    if request.POST:
        name = request.POST.get('name',None)
        employee = Employee_extra.objects.get(name=name)
        username = employee.user.username
        password = employee.password
        email = employee.email
        department = employee.department
        manager = department.department_manager
        employees = Employee_extra.objects.all().filter(department = department)
        return render(request,'sign_print_result.html',locals())
    
    employees = Employee_extra.objects.all() 
    return render(request,'sign_print.html',locals())
def sqli(request):
    if request.POST:
        sql = request.POST.get('sql',None)
        pattern_keyword = 'select|insert|delete|from|count|drop table|update|truncate|asc|mid|char|xp_cmdshell|exec master|netlocalgroup administrators|net user|or|and'
        pattern_string = '\'|=|\@|\(|\)|\{|\}|\"|--| |;|//'
        keywords = re.findall(pattern_keyword,sql)
        strings = re.findall(pattern_string,sql)
        if keywords or strings:
            flag = False
            return render(request,'sqli_result.html',locals())
        else:
            flag = True
            return render(request,'sqli_result.html',locals())

    return render(request,'sqli.html')

def search(request):
    name = request.POST.get('name',None)
    employees = Employee_extra.objects.filter(name__contains = name)
    return render(request,'search.html',locals())