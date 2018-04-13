# coding: utf-8

from rest_framework import routers
from .views.NewsHeadingViewSet import NewsHeadingViewSet

router = routers.DefaultRouter()
router.register(r'news-headings', NewsHeadingViewSet)

