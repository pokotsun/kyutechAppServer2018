# coding: utf-8

from rest_framework import serializers

from ..models import News
from ..const import SCRAPE_BASE_URL 

class NewsSerializer(serializers.ModelSerializer):
    infos = serializers.SerializerMethodField()
    attachement_infos = serializers.SerializerMethodField()
        
    class Meta:
        model = News
        fields = ('news_heading', 'infos', 'attachement_infos')

    def get_infos(self, obj):
        field_names = obj.news_heading.decode_field_names() 
        infos = obj.decode_infos()
        #print(f"infos: {infos}\n\n")

        rtn = {} # 初期化
        for (field_name, info) in zip(field_names, infos):
            rtn[field_name] = info   

        return rtn

    def get_attachement_infos(self, obj):
        field_names = obj.news_heading.get_attachement_field_names()
        attachement_titles = obj.decode_attachement_titles()
        attachement_urls = obj.decode_attachement_urls()

        print(f"attachement_infos: {attachement_titles} : {attachement_urls}")
        rtn = {} #初期化
        #for i in range(attachement_count):        
        for (field_name, title, url) in zip(field_names, attachement_titles, attachement_urls):
        #for i,(title, url) in enumerate(zip(attachement_titles, attachement_urls)):
            rtn[field_name] = {"title": title, "url": f"{SCRAPE_BASE_URL}{url}"}

        return rtn
