from django.contrib import admin
from django.urls import include, path
from rest_framework import urls

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include(urls)),
]