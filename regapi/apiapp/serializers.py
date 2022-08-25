from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Song, Singer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'singer_name', 'gender', 'songs']
