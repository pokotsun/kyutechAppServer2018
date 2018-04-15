# coding: utf-8

from rest_framework import routers
from .views.NewsHeadingViewSet import NewsHeadingViewSet
from .views.NewsViewSet import NewsViewSet

router = routers.DefaultRouter()
router.register(r'news-headings', NewsHeadingViewSet)
router.register(r'news', NewsViewSet)
