# coding: utf-8
from rest_framework import routers
from .views.NewsHeadingViewSet import NewsHeadingViewSet
from .views.NewsViewSet import NewsViewSet, FilteredNewsViewSet
from django.conf.urls import url
from django.urls import path

app_name = "api"

router = routers.DefaultRouter()
router.register(r'news-headings', NewsHeadingViewSet)
#router.register(r'news', NewsViewSet)

urlpatterns = [
    path(r'news/code:<int:code>', FilteredNewsViewSet.as_view()),
]

