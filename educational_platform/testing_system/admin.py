from django.contrib import admin

from .models import Answer, Question, Test

admin.site.register(Test),
admin.site.register(Question),
admin.site.register(Answer),
