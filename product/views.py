from django.shortcuts import render
from product.serializer import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.product_handler import update_product_info

from .models import Product


class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductAddView(APIView):
    def post(self, request, *args, **kwargs):
        data = ProductSerializer(data=request.data)
        if not data.is_valid():
            return Response(data=data.errors, status=status.HTTP_400_BAD_REQUEST)
        data.save()
        return Response({'message': 'Product add successfully'}, status=status.HTTP_201_CREATED)


class ProductUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=self.kwargs['product_id'])
        data = ProductSerializer(data=request.data)
        if not data.is_valid():
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        update_product_info(data, product)
        return Response({'message': 'Updated Successfully'}, status=status.HTTP_200_OK)


class ProductDeleteView(APIView):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id=self.kwargs['product_id'])
        product.delete()
        return Response({'message': 'Deleted Successfully'}, status=status.HTTP_200_OK)

