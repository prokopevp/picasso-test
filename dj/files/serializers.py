from rest_framework import serializers

from files.models import File
from files.tasks import process_file


class FileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    file = serializers.FileField()
    uploaded_at = serializers.DateTimeField(read_only=True)
    processed = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        file = File.objects.create(**validated_data)
        process_file.delay(file.id)
        return file
