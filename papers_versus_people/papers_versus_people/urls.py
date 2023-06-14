from django.contrib import admin
from django.urls import path, include

from .routers import router

api_urls = router.urls + [
    path("accounts/", include("accounts.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include((api_urls, "api"), namespace="v1")),
]
