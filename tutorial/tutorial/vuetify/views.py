from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from rest_framework import permissions


class VuetufyViewSet(APIView):
  # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  renderer_classes = [TemplateHTMLRenderer]
  template_name = 'index.html'


  def get(self, request):
    return Response({'share':True})