from rest_framework import serializers
from .models import Datatable
from django.contrib.auth import get_user_model

class DatatableSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Datatable
        fields = ('id','user','text', 'number', 'data', 'volume','image')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username','password')
