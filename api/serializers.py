from rest_framework import serializers
from . import models

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)
    class Meta:
        model = models.Group
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    user_permissions = PermissionSerializer(many=True)
    class Meta:
        model = models.User
        # fields = '__all__'
        exclude = ('password', 'date_joined', 'last_login')
