import uuid

from django.db import models


# Create your models here.
class Info(models.Model):
    class Meta:
        db_table = "information"

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=32)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
