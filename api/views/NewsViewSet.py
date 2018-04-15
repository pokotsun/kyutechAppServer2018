from rest_framework import generics

from rest_framework import viewsets
from ..models import News
from ..serializers.NewsSerializer import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class FilteredNewsViewSet(generics.ListAPIView):
    #filter_fields = ('pk','news_heading')
    serializer_class = NewsSerializer

    def get_queryset(self):
        news_heading_code = self.kwargs['code']
        if news_heading_code is not None:
            return News.objects.filter(news_heading__news_heading_code__contains=news_heading_code)
        else: 
            return News.objects.all() 
            
