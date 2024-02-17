from django.db import models

class Storage(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
