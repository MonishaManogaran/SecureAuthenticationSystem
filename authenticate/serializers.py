from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class ResgisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model=CustomUser
        fields=('email','firstname','lastname','phonenumber','password')

        def create(self, validated_data):
            user=CustomUser.objects.create_user(
                email=validated_data['email'],
                firstname=validated_data['firstname'],
                lastname=validated_data['lastname'],
                password=validated_data['password'],
                phonenumber=validated_data['phonenumber']
            )
            return user
        
        

