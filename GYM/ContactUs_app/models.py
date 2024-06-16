from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    message = models.TextField(default="", null=True)

    # def __str__(self):
    #     return self.message
