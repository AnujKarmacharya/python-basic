from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = (
            "id",
            "name",
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
            "id",
            "name",
            "price",
            "description",
            "category",
        )
