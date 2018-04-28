from rest_framework import generics

from rest_framework import viewsets
from ..models import UserSchedule
from ..serializers import UserScheduleSerializer

class UserScheduleViewSet(viewsets.ModelViewSet):
    queryset = UserSchedule.objects.all()
    serializer_class = UserScheduleSerializer

    # 一覧表示は必要ないため用意しない
    def list(self, request):
        pass

# フィルタリングされたNewsを表示する
# class FilteredNewsViewSet(generics.ListAPIView):
#     serializer_class = NewsSerializer
#
#     def get_queryset(self):
#         news_heading_code = self.kwargs['code']
#         # これでusernameパラムとして取得できる
#         #print(f"ゆーざーねーむ: {self.request.query_params.get('username', None)}")
#
#         # NewHeadingコードの存在確認
#         if news_heading_code is not None:
#             return News.filter_by_news_heading_code(news_heading_code)
#         else:
#             return None
