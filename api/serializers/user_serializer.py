from rest_framework import serializers

from ..models.user import User
from ..models.school_year import SchoolYear
from ..models.department import Department 

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')

    def update(self, instance, validated_data):

        instance.school_year = validated_data["school_year"]
        instance.department = validated_data["department"]
        instance.save()
        return instance

    def create(self, validated_data):
        new_user = User(
            school_year = validated_data["school_year"],
            department = validated_data["department"]
        )
        
        new_user.save()
        return new_user
