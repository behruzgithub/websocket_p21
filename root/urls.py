from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("apps.urls")),
    path("behruz/", admin.site.urls),
]