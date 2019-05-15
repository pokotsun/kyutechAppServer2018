from django.shortcuts import render

from rest_framework import viewsets
from ..models import UserImpression
from ..serializers import UserImpressionSerializer

class UserImpressionViewSet(viewsets.ModelViewSet):
    queryset = UserImpression.objects.all().order_by('id').reverse()
    serializer_class = UserImpressionSerializer

    # 詳細表示は必要ないため用意しない
    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
