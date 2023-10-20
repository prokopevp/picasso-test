from rest_framework.views import APIView

from files.serializers import FileSerializer
from rest_framework.response import Response
from rest_framework import status

from files.models import File


class UploadFile(APIView):
    serializer_class = FileSerializer

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileList(APIView):
    serializer_class = FileSerializer

    def get(self, request):
        files = File.objects.all()
        f_serializer = FileSerializer(files, many=True)

        return Response(f_serializer.data)