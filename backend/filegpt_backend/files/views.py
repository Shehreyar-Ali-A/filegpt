from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UploadedFile
from .serializers import UploadedFileSerializer

class FilesView(APIView):
    def post(self, request, format=None):
        file_serializer = UploadedFileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, file_id, format=None):
        file_obj = get_object_or_404(UploadedFile, pk=file_id)

        file_obj.delete()

        return JsonResponse({'message': 'File deleted successfully'}, status=204)

class HealthCheck(APIView):
    def get(self, request):
        print("Health check working")
        return Response("Working", status=status.HTTP_200_OK)
