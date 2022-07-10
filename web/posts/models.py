from pyexpat import model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    remark = models.CharField(max_length=120, blank=True)
