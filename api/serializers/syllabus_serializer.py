from rest_framework import serializers

from ..models import Syllabus

class SyllabusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Syllabus
        exclude = ('created_at',) # created_atのみ除く
