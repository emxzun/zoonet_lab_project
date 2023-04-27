from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.description
