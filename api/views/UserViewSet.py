from django.shortcuts import render

from rest_framework import viewsets
from ..models import User
from ..serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # 一覧表示は必要ないため用意しない
    def list(self, request):
            pass
