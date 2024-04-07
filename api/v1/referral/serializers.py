from rest_framework import serializers
from referral.models import *

class CreateRegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    password=serializers.CharField()

class ListRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=(
            'id',
            'name',
            'email',
            'referral_code',
            'timestamp',
        )
   