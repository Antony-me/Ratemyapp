from rest_framework import serializers
from .models import Profile, Post

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ="__all__"

class MerchSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ="__all__"