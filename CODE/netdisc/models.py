from django.db import models

from CODE import settings

# Create your models here.

class Photo(models.Model):
    image = models.FileField(storage=settings.UPLOAD_STORAGE, upload_to='netdisc/photo/')
    location = models.CharField(max_length=16, help_text='照片拍摄地', blank=True, default='')
    desc = models.TextField(help_text='照片描述', blank=True, default='')
