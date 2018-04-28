from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from django.http import Http404
from rest_framework import viewsets
from ..models import UserSchedule, User
from ..serializers import UserScheduleSerializer

class UserScheduleViewSet(viewsets.ModelViewSet):
    queryset = UserSchedule.objects.all()
    serializer_class = UserScheduleSerializer

    # 一覧表示は必要ないため用意しない
    def list(self, request):
        pass

# フィルタリングされたUserScheduleを表示する
class FilteredUserScheduleViewSet(generics.ListAPIView):
    serializer_class = UserScheduleSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        # これでusernameパラムとして取得できる
        #print(f"ゆーざーねーむ: {self.request.query_params.get('username', None)}")

        print(f"{user_id}")
        # user_idの存在確認
        user = None
        if user_id is not None:
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                raise Http404("Your Requested User Id Does not Exist!!")
            return UserSchedule.objects.filter(is_valid=True, user=user)
            # return News.filter_by_news_heading_code(news_heading_code)
        else:
            return None
