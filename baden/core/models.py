from django.db import models


class Apartment(models.Model):
    title = models.CharField(max_length=255)


class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images")
