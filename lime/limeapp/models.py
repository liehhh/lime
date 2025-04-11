from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User



class Song(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    audio_file = models.FileField(upload_to='songs/', validators=[FileExtensionValidator(allowed_extensions=['mp3','wav'])], default='song.mp3')

    def __str__(self):
        return self.title
