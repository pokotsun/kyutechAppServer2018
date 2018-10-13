from rest_framework import serializers

from ..models.user import User
from ..models.school_year import SchoolYear
from ..models.department import Department 

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')

    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def update(self, instance, validated_data):

        instance.school_year = SchoolYear.objects.get(unique_code=validated_data["school_year"])
        instance.department = Department.objects.get(unique_code=validated_data["department"])
        instance.save()
        return instance

    def create(self, validated_data):
        new_user = User(
            school_year = SchoolYear.objects.get(unique_code=validated_data["school_year"]),
            department = Department.objects.get(unique_code=validated_data["department"])
        )
        
        new_user.save()
        return new_user
