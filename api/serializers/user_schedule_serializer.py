from rest_framework import serializers

from ..models import UserSchedule
from ..serializers.syllabus_serializer import SyllabusSerializer
from ..serializers.user_serializer import UserSerializer

class UserScheduleSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # syllabus = SyllabusSerializer()

    class Meta:
        model = UserSchedule
        exclude = ('created_at', 'updated_at') # created_atのみ除く
