from rest_framework import generics

from rest_framework import viewsets
from ..models import News
from ..serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# フィルタリングされたNewsを表示する
class FilteredNewsViewSet(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        news_heading_code = self.kwargs['code']
        # これでusernameパラムとして取得できる
        #print(f"ゆーざーねーむ: {self.request.query_params.get('username', None)}")

        # NewHeadingコードの存在確認
        if news_heading_code is not None:
            return News.filter_by_news_heading_code(news_heading_code)
        else:
            return None
