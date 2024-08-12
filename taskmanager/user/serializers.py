from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'username', 'phone', 'first_name', 'last_name', 'gender', 'role', 'password', 'password_confirm']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            phone=validated_data['phone'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            gender=validated_data.get('gender', ''),
            role=validated_data.get('role', User.RoleChoices.EMPLOYEE),
            password=validated_data['password']
        )
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'phone', 'first_name', 'last_name', 'gender', 'role']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class UserDeleteSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()

    def delete(self):
        user_id = self.validated_data['user_id']
        try:
            user = User.objects.get(user_id=user_id)
            user.delete()
            return True
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")
        

# myapp/serializers.py



class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    password = serializers.CharField()

