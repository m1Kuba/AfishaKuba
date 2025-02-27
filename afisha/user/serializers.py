from . import models
from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=6)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6)
    comfirm_password = serializers.CharField(min_length=6)

    def validate(self, data):
        if data['password'] != data['comfirm_password']:
            raise serializers.ValidationError('Passwords do not match')
        return data

    def validate_username(self, username):
        try:
            User.objects.filter(username=username).exists()
        except User.DoesNotExist:
            return username
        raise serializers.ValidationError('User already exists')


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=6)
    password = serializers.CharField(min_length=6)

class SMSCodeSerializer(serializers.ModelSerializer):
    sms_code = serializers.CharField(max_length=6)
