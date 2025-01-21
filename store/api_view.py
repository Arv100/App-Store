from rest_framework.response import Response
from .models import App
from .serializer import AppSerializer, UserSerializer
from .models import CustomUser, App
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class AppListAPI(generics.ListCreateAPIView):
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return App.objects.all()

class AppDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated]