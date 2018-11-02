from django.db import models
from django.utils import timezone


class ArtifactDetail(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    room_no = models.IntegerField(default = 0)
    artifact_no = models.IntegerField(default = 0)
    artifact_name = models.CharField(max_length=200)
    artifact_description = models.TextField()

    excavated_date = models.DateField(default=timezone.localdate)
    artifact_year = models.CharField(max_length=40,default='NA')



    def __str__(self):
        return self.artifact_name
