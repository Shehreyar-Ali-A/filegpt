from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from chat.models import models
from chat.serializer import ChatSerializer
from .file_processor import process_file

class FilesView(APIView):
    def post(self, request, format=None):
        """
        This function is responsible for the following things
            1. Uploading the file to a local dir for temp storage
            2. Create a new chat object in the database
            3. Preforming OCR (if required)
            4. Extracting text from the file 
            5. Creating chunks
            6. Creating the embeddings from the chunks
            7. Storing the embeddings in pinecone db
        """
        file_serializer = UploadedFileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_instance = file_serializer.save()
            print("\n\n",file_instance.id,"\n\n")

            
            process_file(file_instance.id)


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
