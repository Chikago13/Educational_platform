from django.contrib import admin

from .models import Group, Student, Teacher

admin.site.register(Teacher),
admin.site.register(Student),
admin.site.register(Group)
