from urllib import response
from .models import Song, Singer
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import RegisterSerializer, SongSerializer, SingerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token

# Create your views here.

class SongView(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SingerView(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user":"New User Registered Successfully!",
            "token": token.key,
        })
