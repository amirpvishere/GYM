from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='trainer')


    def __str__(self):
        return self.name
