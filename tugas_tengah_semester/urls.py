from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("reload/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("authentication/", include("authentication.urls")),
    path("tender/", include("tender.urls")),
    path("agriculture/", include("agriculture.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)