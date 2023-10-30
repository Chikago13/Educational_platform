from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("user/", include("user.urls")),
    # path("student/", include("student.urls")),
    # path("teacher/", include("teacher.urls")),
    # path("group/", include("group.urls")),
    # path("courses/", include("courses.urls")),
]

