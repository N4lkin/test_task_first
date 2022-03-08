from rest_framework import serializers
from .models import *


# Сериализатор должен принимать на вход фразу, и если совпала - отдать сообщение
class SetSecretCode(serializers.ModelSerializer):

    class Meta:
        model = SecretKey
        fields = ('phrase', 'code', 'TTL', 'secret_key')


class SecretCodeForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretKey
        fields = ('phrase', )
