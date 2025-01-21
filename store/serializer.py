from rest_framework import serializers
from .models import App, CustomUser


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
