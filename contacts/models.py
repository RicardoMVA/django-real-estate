from django.db import models

from datetime import datetime

# Create your models here.


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(
        default=datetime.now,
        blank=True
    )
    # any person will be able to make a contact, but if the
    # contact is made by an logged user, then this will
    # take the user currently logged in
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
