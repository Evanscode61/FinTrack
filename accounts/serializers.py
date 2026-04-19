from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'password',
                  'password2',
                  ]
    def validate_email(self, value):
        return value.lower()

    def validate(self , data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        return data
    def validate_phone_number(self, value):
        if value and not value.isdigit():
            raise serializers.ValidationError({'phone_number': 'Phone number must be digits!'})
        return value


    def create(self, validated_data):
        validated_data.pop('password2')
        return User. objects.create_user(**validated_data)