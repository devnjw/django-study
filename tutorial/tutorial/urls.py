from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# 우리가 만든 API를 자동으로 라우팅합니다.
# 그리고 API 탐색을 위해 로그인 URL을 추가했습니다.
urlpatterns = [
    path('', include(router.urls)),
    path('auth-api', include('rest_framework.urls', namespace='rest_framework'))
]