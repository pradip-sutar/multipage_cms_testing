from rest_framework import serializers
from .models import Menu, Submenu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class SubmenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submenu
        fields = '__all__'
