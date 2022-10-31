from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("authentication/", include("authentication.urls")),
    path("tender/", include("tender.urls")),
    path("marine/", include("marine.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
