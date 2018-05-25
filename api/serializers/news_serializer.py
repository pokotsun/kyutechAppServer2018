# coding: utf-8

from rest_framework import serializers

from ..serializers import NewsHeadingSerializer
from ..models import News
from ..const import SCRAPE_NEWS_URL

class NewsSerializer(serializers.ModelSerializer):
    # news_heading = NewsHeadingSerializer()
    infos = serializers.SerializerMethodField()
    attachment_infos = serializers.SerializerMethodField()
    news_heading_code = serializers.SerializerMethodField()
    source_url = serializers.SerializerMethodField()
    

    class Meta:
        model = News
        fields = ('id', 'news_heading_code', 'source_url', 'infos', 'attachment_infos')

    def get_news_heading_code(self, obj):
        return obj.news_heading.news_heading_code
    def get_source_url(self, obj):
        return f"{SCRAPE_NEWS_URL}{obj.url_params}" 

    def get_infos(self, obj):
        field_names = obj.news_heading.decode_field_names()
        infos = obj.decode_infos()
        rtn = [] # 初期化
        for (field_name, info) in zip(field_names, infos):
            rtn.append({"title": field_name, "content": info})

        return rtn

    def get_attachment_infos(self, obj):
        field_names = obj.news_heading.get_attachment_field_names()
        attachment_titles = obj.decode_attachment_titles()
        attachment_urls = obj.decode_attachment_urls()

        rtn = [] #初期化
        for (field_name, link_name, url) in zip(field_names, attachment_titles, attachment_urls):
            rtn.append({"title": field_name, "link_name": link_name, "url": url})

        return rtn
