from django.contrib import admin
from django.urls import path
from rest.views import RestListAPI

urlpatterns = [
    path('admin/', admin.site.urls),
	path('api/rest/', RestListAPI.as_view())
]