from django.shortcuts import render
from django.http import JsonResponse
from .models import UserDetails
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserDetailsSerializer
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from rest_framework import viewsets
from .serializers import *
# Create your views here.


class UserDetailsView(APIView):
    permissions_classes = (AllowAny)
    serializer_class = UserDetailsSerializer

    def get(self, request):
        detail = [{"fullname": detail.fullname, "email": detail.email, "password": detail.password, "dob": detail.dob, "gender": detail.gender, "timestamp": detail.timestamp}
                  for detail in UserDetails.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
