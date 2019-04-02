from django.db import models


class Contact(models.Model):
    user_id = models.IntegerField()
    listing = models.IntegerField()
    listing_id = models.IntegerField()
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    message = models.TextField()
    contact_date = models.DateField()

    def __str__(self):
        return self.name





