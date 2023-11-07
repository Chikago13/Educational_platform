from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("user/", include("user.urls")),
    # path("study/", include("study.urls")),
    # path("mentorship/", include("mentorship.urls")),
    # path("testing_system/", include("testing_system.urls")),
]
