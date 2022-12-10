from rest_framework import serializers
from FileUpload.models import Files

class fileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Files
        fields = ['description', 'file']