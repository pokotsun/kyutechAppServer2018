# coding: utf-8

from rest_framework import serializers

from ..models import News
from ..const import SCRAPE_NEWS_URL

class NewsSerializer(serializers.ModelSerializer):
    infos = serializers.SerializerMethodField()
    attachement_infos = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('infos', 'attachement_infos')

    def get_infos(self, obj):
        field_names = obj.news_heading.decode_field_names()
        infos = obj.decode_infos()
        rtn = [] # 初期化
        for (field_name, info) in zip(field_names, infos):
            rtn.append({"title": field_name, "content": info})

        return rtn

    def get_attachement_infos(self, obj):
        field_names = obj.news_heading.get_attachement_field_names()
        attachement_titles = obj.decode_attachement_titles()
        attachement_urls = obj.decode_attachement_urls()

        rtn = [] #初期化
        for (field_name, link_name, url) in zip(field_names, attachement_titles, attachement_urls):
            rtn.append({"title": field_name, "link_name": link_name, "url": url})

        return rtn
