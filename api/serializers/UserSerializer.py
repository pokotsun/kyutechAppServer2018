from rest_framework import serializers

from ..models.user import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'pk', 'school_year', 'department', 'created_at', 'updated_at',
        )
