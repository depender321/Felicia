from rest_framework import serializers
from .models import Product

class PriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name','price')