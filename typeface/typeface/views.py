from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer


@api_view(['POST'])
def upload_file(request):
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def read_file(request, file_id):
    try:
        file_obj = File.objects.get(file_id=file_id)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FileSerializer(file_obj)
    return Response(serializer.data)


@api_view(['PUT'])
def update_file(request, file_id):
    try:
        file_obj = File.objects.get(file_id=file_id)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FileSerializer(file_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_file(request, file_id):
    try:
        file_obj = File.objects.get(file_id=file_id)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    file_obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def list_files(request):
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)