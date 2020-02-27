from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=255)


class Description(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=255, null=True)
    status = models.ForeignKey(
        'Status',
        on_delete=models.CASCADE,
        )
    created_at = models.DateTimeField(auto_now_add=True)
