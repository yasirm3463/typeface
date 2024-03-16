from django.db import models
import uuid


class File(models.Model):
    file_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    size = models.PositiveIntegerField()
    file_type = models.CharField(max_length=100)