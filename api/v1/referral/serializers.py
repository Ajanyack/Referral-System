from rest_framework import serializers
from referral.models import *

class CreateRegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    password=serializers.CharField()