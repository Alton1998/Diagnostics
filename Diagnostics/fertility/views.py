from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Fertility
from .serializer import FertilitySerializer

class FertilityAPIView(APIView):
    def get(self, request):
        data= Fertility.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer = FertilitySerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FertilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)