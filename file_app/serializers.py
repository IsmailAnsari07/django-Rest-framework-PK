from rest_framework import serializers
from .models import FileData

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileData
        fields = ('file', 'remark', 'timestamp')