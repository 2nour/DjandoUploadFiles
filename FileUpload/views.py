from rest_framework import viewsets
from django.http import HttpResponse
from FileUpload.serializers import   fileSerializer
from FileUpload.models import Files

class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = fileSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        description = request.data['description']
        Files.objects.create(description=description, file=file)
        return HttpResponse({'message': 'file added created'}, status=200)