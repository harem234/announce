from .models import Announcement
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        self.request.user.pk
    
class AnnouncementSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(many=False, read_only=False)
    class Meta:
        model = Announcement
        fields = ('id', 'title', 'description', 'view_count', 'user')


