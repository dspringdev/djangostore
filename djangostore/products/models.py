from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length = 2083) # Max length for url


class Offer(models.Model):
    code = models.CharField(max_length = 10, blank = False, null = False)
    description = models.CharField(max_length = 255)
    discount = models.FloatField(blank = False, null = False)

    def __str(self):
        return "Offer: {}".format(self.description)
