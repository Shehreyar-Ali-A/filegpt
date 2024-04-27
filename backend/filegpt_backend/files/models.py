from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage

# Create your models here.


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    upload_url = models.URLField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    
    def save(self, *args, **kwargs):
        self.upload_url = self.file.url.split("?")[0]
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.file and default_storage.exists(self.file.name):
            self.file.delete(save=False)
        super().delete(*args, **kwargs)