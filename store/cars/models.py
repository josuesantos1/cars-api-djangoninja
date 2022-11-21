from django.db import models

import uuid

class Cars(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )

    title = models.CharField(
        max_length=256,
    )

    model = models.CharField(
        max_length=64
    )

    price = models.FloatField(
        blank=False,
        null=False
    )

    isPublic = models.BooleanField(
        default=True
    )

    # TODO: use reference with user
