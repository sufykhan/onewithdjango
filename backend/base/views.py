from django.shortcuts import render

from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer
from .productsData import products
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    return Response({"message":"high"})

@api_view(['GET'])
def getProducts(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
    product=Product.objects.get(_id=pk)
    serializer=ProductSerializer(product,many=False)
    #serializer.data is in the form of dictionary
    return Response(serializer.data)
