from rest_framework import serializers
from .models import ApartmentImage, Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'
