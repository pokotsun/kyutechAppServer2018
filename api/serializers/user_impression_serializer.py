from rest_framework import serializers

from ..models import UserImpression

class UserImpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImpression
        fields = (
            "id", "timestamp", "which_os", "evaluation", 
            "opinion", "request_pd", "reply"
        )

    
