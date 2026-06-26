from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ContactMessage, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'role')

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ('id', 'full_name', 'email', 'company', 'message', 'created_at', 'read')
        read_only_fields = ('id', 'created_at', 'read')