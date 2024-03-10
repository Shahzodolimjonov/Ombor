from rest_framework import serializers
from .models import *

# Django modellarini, Pythonning ma'lumot turlariga o'girish va ularni JSON, XML
# turlariga osonroq aylandirish uchun ishlatiladi.


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['name']


class WarehouseStockSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()

    class Meta:
        model = WarehouseStock
        fields = ['warehouse', 'material', 'remainder', 'price']


class ProductMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()

    class Meta:
        model = ProductMaterial
        fields = ['material', 'quantity']


class ProductSerializer(serializers.ModelSerializer):
    # product_materials maydoni uchun ichki ProductMaterialSerializer ni o'z ichiga oladi.
    product_materials = ProductMaterialSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'product_materials']

