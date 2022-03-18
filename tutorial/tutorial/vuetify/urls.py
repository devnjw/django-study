from django.urls import path, include

from .views import VuetufyViewSet

urlpatterns = [
    path('vuetify/', VuetufyViewSet.as_view()),
]
