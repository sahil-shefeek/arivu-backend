from django.db import models


class GPTQuery(models.Model):
    query = models.TextField()
