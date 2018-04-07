from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('bio', 'job_title')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    userprofile = UserProfileSerializer(many=False)
    class Meta:
        model = User
        fields = ('url' ,'username', 'email', 'userprofile')
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }


