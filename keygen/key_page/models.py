import uuid
from django.db import models


# Главная модель
class SecretKey(models.Model):
    code = models.CharField(null=False, blank=False, max_length=20, verbose_name='Phrase opening code.'
                                                                                 ' Up to 20 characters')
    phrase = models.TextField(null=False, blank=False, verbose_name='Phrase')
    secret_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TTL = models.PositiveIntegerField(default=3600, verbose_name='Time phrase life')
