from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("authentication/", include("authentication.urls")),
    path("tender/", include("tender.urls")),
    path("waste/", include("waste.urls")),
]
