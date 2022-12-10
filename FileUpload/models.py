from django.db import  models


def upload_path(instance, filname):
    return '/'.join(['files',  filname])


class Files(models.Model):
    description = models.CharField(max_length=32, blank=False)
    file = models.FileField(blank=True, null=True, upload_to=upload_path)
