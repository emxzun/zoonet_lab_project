from django.db import models

<<<<<<< HEAD
=======
from django.db import models

>>>>>>> 489992a1922f2266d32ed71161681565cfd08ae0

class News(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
<<<<<<< HEAD
        return self.pk
=======
        return self.description
>>>>>>> 489992a1922f2266d32ed71161681565cfd08ae0
