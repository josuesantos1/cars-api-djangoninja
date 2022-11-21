from django.db import models

import uuid

class User(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
    )

    email = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )

    password = models.TextField(
        null=False,
        blank=False
    )
