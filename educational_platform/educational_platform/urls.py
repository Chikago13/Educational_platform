from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("user.urls")),
    path("study/", include("study.urls")),
    path("mentorship/", include("mentorship.urls")),
    path("testing_system/", include("testing_system.urls")),
]
