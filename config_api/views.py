from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, WarehouseStock
from .serializers import ProductSerializer, WarehouseStockSerializer

# result
class ProductionInfo(APIView):
    def get(self, request):
        products = Product.objects.all()
        response_data = []

        for product in products:
            product_materials = []
            for product_material in product.productmaterial_set.all():
                warehouse_stock = WarehouseStock.objects.filter(material=product_material.material)
                if warehouse_stock.exists():
                    warehouse_stock_serializer = WarehouseStockSerializer(warehouse_stock, many=True)
                    product_material_data = warehouse_stock_serializer.data[0]
                    product_material_data['material'] = product_material.material.name
                    product_material_data['quantity'] = product_material.quantity
                    product_materials.append(product_material_data)

            response_data.append({
                'product_name': product.name,
                'product_materials': product_materials
            })

        return Response(response_data, status=status.HTTP_200_OK)
