from django.shortcuts import render

from rest_framework import viewsets
from ..models import News
from ..serializers.NewsSerializer import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
