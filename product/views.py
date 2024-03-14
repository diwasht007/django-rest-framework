from django.shortcuts import render
from .models import Product
from product.api.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status

# from django.http import JsonResponse
# Create your views here.

# def product(request):
#     products = Product.objects.all()
#     context = {
#         'products': list(products.values()),

#     }
#     return JsonResponse(context)

# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {
        
#         'name': product.product_name,
#         'price': product.price,
#         'description': product.description,
#     }
#     return JsonResponse(context)


@api_view(['GET','POST'])
def product(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

@api_view(['GET','PUT','DELETE'])
def product_detail(request, pk):
    if request.method == 'GET':
        try:
            product_detail = Product.objects.get(pk=pk)
        except:
            return Response({'Error':'Product not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product_detail)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        product_detail = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product_detail,data = request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        product_detail = Product.objects.get(pk=pk)
        product_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


