from rest_framework import serializers
from api.models import Data
from django.contrib.auth.models import User


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields="__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)