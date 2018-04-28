# coding: utf-8
from rest_framework import routers
from .views.NewsHeadingViewSet import NewsHeadingViewSet
from .views.NewsViewSet import NewsViewSet, FilteredNewsViewSet
from .views.SyllabusViewSet import SyllabusViewSet, FilteredSyllabusViewSet
from .views.UserViewSet import UserViewSet
from .views.UserScheduleViewSet import UserScheduleViewSet, FilteredUserScheduleViewSet
from django.conf.urls import url
from django.urls import path

app_name = "api"

urlpatterns = [
    #path(r'news/code:<int:code>', FilteredNewsViewSet.as_view()),
    path(r'news/code-<int:code>/', FilteredNewsViewSet.as_view()),
    path(r'syllabuses/day-<str:day>/period-<str:period>', FilteredSyllabusViewSet.as_view()),
    path(r'user-schedules/user-<int:user_id>/', FilteredUserScheduleViewSet.as_view())
]

router = routers.DefaultRouter()
router.register(r'news-headings', NewsHeadingViewSet)
router.register(r'syllabuses', SyllabusViewSet)
router.register(r'users', UserViewSet)
router.register(r'user-schedules', UserScheduleViewSet)

router.register(r'news', NewsViewSet)
