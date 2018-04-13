# coding: utf-8

from rest_framework import serializers

from ..models import NewsHeading

class NewsHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsHeading
        fields = (
        'news_heading_code',
        'short_name', 
        'name',
        'color_code',
        'updated_at')
