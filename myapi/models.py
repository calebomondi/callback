from django.db import models

# Create your models here.
class MpesaCB(models.Model):
    received_at = models.DateTimeField(auto_now_add=True,null=True)
    data = models.JSONField()