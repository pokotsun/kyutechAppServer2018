from django.shortcuts import render

from rest_framework import viewsets
from ..models import NewsHeading
from ..serializers.NewsHeadingSerializer import NewsHeadingSerializer

class NewsHeadingViewSet(viewsets.ModelViewSet):
    queryset = NewsHeading.objects.all()
    serializer_class = NewsHeadingSerializer
