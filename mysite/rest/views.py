from django.shortcuts import render
from rest_framework.response import Response
from .models import Rest
from rest_framework.views import APIView
from .serializers import RestSerializer

class RestListAPI(APIView):
    def get(self, request):
        queryset = Rest.objects.all()
        print(queryset)
        serializer = RestSerializer(queryset, many=True)
        return Response(serializer.data)