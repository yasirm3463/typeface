from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file_id', 'file_name', 'created_at', 'size', 'file_type']