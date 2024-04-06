import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True