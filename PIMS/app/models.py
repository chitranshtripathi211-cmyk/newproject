from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# creating a database table for storing the details of the project ORM 
class Item (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    quantity = models.IntegerField()
    min_quantity = models.IntegerField()
    expiry_date = models.DateField( null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
