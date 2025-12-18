from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """ Сериализатор для пользователя. """

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone_num', ]


class UserCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания пользователя. """

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password"]

    def create(self, validated_data):
        user: CustomUser = CustomUser.objects.create(
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user
