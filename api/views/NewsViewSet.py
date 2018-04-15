from rest_framework import generics

from rest_framework import viewsets
from ..models import News
from ..serializers.NewsSerializer import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class FilteredNewsViewSet(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        news_heading_code = self.kwargs['code']
        # これでusernameパラムとして取得できる
        #print(f"ゆーざーねーむ: {self.request.query_params.get('username', None)}")
        if news_heading_code is not None:
            return News.objects.filter(news_heading__news_heading_code__contains=news_heading_code)
        else: 
            return News.objects.all() 
            
