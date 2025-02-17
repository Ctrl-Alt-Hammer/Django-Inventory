from django.db import models

class Item(models.Model):
    image = models.ImageField(upload_to='images/', default='images/default.png')
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
