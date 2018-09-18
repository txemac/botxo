from django.db import models
from django.utils import timezone


class Message(models.Model):
    dt_created = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    @classmethod
    def get_random(cls):
        return cls.objects.order_by('?').first().text

    def __str__(self):
        return self.text
