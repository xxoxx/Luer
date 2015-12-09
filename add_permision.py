from hr.models import Department,Employee_extra,Attendence,Salary
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
content_type = ContentType.objects.get_for_model(Employee_extra)
permission = Permission.objects.create(codename='search_info_all',name='search_info_all',content_type=content_type)
