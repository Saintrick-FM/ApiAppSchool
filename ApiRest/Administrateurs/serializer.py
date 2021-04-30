from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', 'is_staff']
        extra_kwargs = {'email': {'required': False},
                        'password': {'write_only': True}}

    def create(self, **validated_data):
        user = Users.objects.create_user(**validated_data)
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
        return user
