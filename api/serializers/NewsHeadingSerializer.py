# coding: utf-8

from rest_framework import serializers

from ..models import NewsHeading

class NewsHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsHeading
        fields = ('short_name', 'name')
