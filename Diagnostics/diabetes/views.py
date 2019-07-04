from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Diabetes
from .serializer import DiabetesSerializer

class DiabetesAPIView(APIView):
    def get(self, request):
        data= Diabetes.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer = DiabetesSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiabetesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)