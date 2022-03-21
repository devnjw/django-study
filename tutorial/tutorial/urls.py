from django.urls import path
from django.conf.urls import include
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'vuetify', VuetufyViewSet.as_view(), basename='vuetify')

# 우리가 만든 API를 자동으로 라우팅합니다.
# 그리고 API 탐색을 위해 로그인 URL을 추가했습니다.
urlpatterns = [
    path('', include('tutorial.vuetify.urls')),
]