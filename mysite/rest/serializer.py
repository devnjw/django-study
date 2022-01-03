from rest_framework import serializers
from .models import Rest

class RestSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Rest        # product 모델 사용
        fields = '__all__'            # 모든 필드 포함