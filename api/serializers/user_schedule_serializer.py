from rest_framework import serializers
from ..models import UserSchedule, User, Syllabus
from ..serializers.syllabus_serializer import SyllabusSerializer
from ..serializers.user_serializer import UserSerializer

class UserScheduleSerializer(serializers.ModelSerializer):
    # postの時はuser_idのみ、 getの時はuser情報すべてを渡せるようにする
    user_id = serializers.PrimaryKeyRelatedField(source='user',  queryset=User.objects.all(), write_only=True)
    # user = UserSerializer(read_only=True)

    syllabus_id = serializers.PrimaryKeyRelatedField(source='syllabus', queryset=Syllabus.objects.all(), write_only=True)
    syllabus = SyllabusSerializer(read_only=True)

    class Meta:
        model = UserSchedule
        fields = ('id', 'user_id', 'syllabus_id', 'syllabus', 'day', 'period', 'quarter', 'memo', 'late_num', 'absent_num')

    def get_user(self, obj):
        return UserSerializer()

    def get_syllabus(self, obj):
        return SyllabusSerializer(obj.syllabus)

    def create(self, validated_data):
        """ Add UserSchedule"""
        new_schedule = UserSchedule(
            user = validated_data['user'],
            syllabus = validated_data['syllabus'],
            day = validated_data['day'],
            period = validated_data['period'],
            quarter = validated_data['quarter'],
            memo = validated_data['memo'],
            is_valid = True,
        )

        print(f"new_schedule: {new_schedule}")

        past_schedules = UserSchedule.objects.filter(
            user = new_schedule.user,
            day = new_schedule.day,
            period = new_schedule.period,
            quarter = new_schedule.quarter,
            is_valid = True,
        ).order_by('updated_at').reverse()

        if past_schedules: # past_schedulesが空でなければ
            past_schedule = past_schedules.last()
            past_schedule.is_valid = False
            past_schedule.save()
            # print(f"\n past_schedule: {past_schedule}\n")

        # print(f"\nnew_schedule: {new_schedule}\n")
        new_schedule.save()

        return new_schedule
        # return Response({"user_id": f"{new_schedule.user}"})
