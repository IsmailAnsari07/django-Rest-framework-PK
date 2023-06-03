from django.db import models

# Create your models here.
class FileData(models.Model):
    file = models.FileField(blank=False, null=False)# if we use blank=False, null=False so this is basically means no blank data and null values.
    remark = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)#It automatically stores the timestamp