from django.contrib import admin

from .models import Article, Course, Image, Specialization, Topic

admin.site.register(Specialization),
admin.site.register(Course),
admin.site.register(Article),
admin.site.register(Image),
admin.site.register(Topic)
