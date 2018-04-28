from rest_framework import serializers

from ..models import UserSchedule, User, Syllabus
from ..serializers.syllabus_serializer import SyllabusSerializer
from ..serializers.user_serializer import UserSerializer

class UserScheduleSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # syllabus = SyllabusSerializer()
    user_id = serializers.PrimaryKeyRelatedField(source='user',  queryset=User.objects.all(), write_only=True)
    user = UserSerializer(read_only=True)
    syllabus_id = serializers.PrimaryKeyRelatedField(source='syllabus', queryset=Syllabus.objects.all(), write_only=True)
    syllabus = SyllabusSerializer(read_only=True)
    # is_valid = serializers.BooleanField(write_only=True)

    class Meta:
        model = UserSchedule
        fields = ('user_id', 'user', 'syllabus_id', 'syllabus', 'day', 'period', 'quarter', 'is_valid')
        # exclude = ('created_at', 'updated_at') # created_atのみ除く

    def get_user(self, obj):
        return UserSerializer()

    def get_syllabus(self, obj):
        return SyllabusSerializer(obj.syllabus)
