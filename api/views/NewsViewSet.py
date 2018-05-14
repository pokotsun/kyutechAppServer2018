from rest_framework import generics

from rest_framework import viewsets
from ..models import News
from ..serializers import NewsSerializer

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

# フィルタリングされたNewsを表示する
class FilteredNewsViewSet(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        news_heading_code = self.kwargs['code']
        # これでusernameパラムとして取得できる
        #print(f"ゆーざーねーむ: {self.request.query_params.get('username', None)}")

        # NewsHeadingCodeの存在確認
        if news_heading_code is not None:
            return News.filter_by_news_heading_code(news_heading_code)
        else:
            return None
