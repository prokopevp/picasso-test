from django.db import models


# Create your models here.

class File(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['uploaded_at']
        verbose_name = 'file'
        verbose_name_plural = 'files'
