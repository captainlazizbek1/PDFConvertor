from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings

class DocxFile(models.Model):
    file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])], null=False, blank=False)

    def __str__(self):
        return self.file.path

