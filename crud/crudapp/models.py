from django.db import models

class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    first_name = models.CharField(max_length=100)  # First name of the record
    last_name = models.CharField(max_length=100)  # Last name of the record
    email = models.EmailField(max_length=254)  # Email address of the record
    phone = models.CharField(max_length=20)  # Phone number of the record
    address = models.TextField(max_length=300)  # Address of the record
    city = models.CharField(max_length=100)  # City of the record
    country = models.CharField(max_length=100)  # Country of the record

    def __str__(self):
        return self.first_name + "   " +  self.last_name
